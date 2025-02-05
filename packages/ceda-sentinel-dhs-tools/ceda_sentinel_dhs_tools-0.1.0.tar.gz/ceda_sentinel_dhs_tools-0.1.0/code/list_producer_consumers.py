from datetime import datetime, timezone, timedelta
import requests
import click
import configparser
from typing import Dict, List
from tabulate import tabulate
from textwrap import fill
import smtplib


def get_instance_name(url: str) -> str:
    """Extract GSS instance name from URL"""
    if not url:
        return "N/A"
    try:
        from urllib.parse import urlparse

        parsed = urlparse(url)
        return parsed.hostname.split(".")[0]
    except:
        return "N/A"


def get_producers(base_url) -> List[Dict]:
    """Get list of producers and return their full details"""
    headers = {"accept": "application/json"}
    try:
        response = requests.get(f"{base_url}/producers", headers=headers)
        response.raise_for_status()
        data = response.json()
        producers = data.get("producers", [])

        gss_instance = get_instance_name(base_url)

        producer_details = []
        for p in producers:
            details = {
                "name": p.get("name"),
                "serviceRootUrl": p.get("source", {}).get("serviceRootUrl"),
                "gssInstance": gss_instance,
                "lastPublicationDate": p.get("source", {}).get("lastPublicationDate"),
                "filter": p.get("source", {}).get("filter"),
            }
            producer_details.append(details)
        return producer_details
    except requests.exceptions.RequestException as e:
        click.echo(click.style(f"Error fetching producers: {e}", fg="red"), err=True)
        return None


def get_consumers(base_url) -> List[Dict]:
    """Get list of consumers and return their full details"""
    headers = {"accept": "application/json"}
    try:
        response = requests.get(f"{base_url}/consumers", headers=headers)
        response.raise_for_status()
        data = response.json()
        consumers = data.get("consumers", [])
        consumer_details = []
        for c in consumers:
            details = {
                "name": c.get("name"),
                "serviceRootUrl": c.get("source", {}).get("serviceRootUrl"),
            }
            consumer_details.append(details)
        return consumer_details
    except requests.exceptions.RequestException as e:
        click.echo(f"Error fetching consumers: {e}")
        return None


def format_table_data(producers, consumer_lookup):
    """Format data for tabulate"""
    table_data = []

    def safe_fill(text, width):
        """Safely fill text with handling for None values"""
        if text is None:
            text = "N/A"
        return fill(str(text), width)

    max_widths = {
        "producer": 25,
        "consumer": 25,
        "url": 30,
        "instance": 15,
        "date": 20,
        "filter": 40,
    }

    for producer in producers:
        base_name = producer["name"].replace("-producer", "")
        consumer = consumer_lookup.get(base_name)

        row = [
            click.style(
                safe_fill(producer.get("name"), max_widths["producer"]),
                fg="cyan",
                bold=True,
            ),
            click.style(
                safe_fill(
                    consumer["name"] if consumer else "No consumer pair",
                    max_widths["consumer"],
                ),
                fg="blue" if consumer else "yellow",
            ),
            safe_fill(producer.get("serviceRootUrl"), max_widths["url"]),
            safe_fill(producer.get("gssInstance"), max_widths["instance"]),
            safe_fill(producer.get("lastPublicationDate"), max_widths["date"]),
            safe_fill(producer.get("filter", "N/A"), max_widths["filter"]),
        ]
        table_data.append(row)

    return table_data


def filter_by_string(producers: List[Dict], filter_string: str) -> List[Dict]:
    """Filter producers by matching string in their filter"""
    if not filter_string:
        return producers
    return [p for p in producers if filter_string in str(p.get("filter", ""))]


def filter_by_date(producers: List[Dict], time_filter: str) -> List[Dict]:
    """Filter producers by LastCreationDate being older/younger than given date"""
    if not time_filter:
        return producers

    try:
        filter_date = datetime.strptime(time_filter, "%Y-%m-%dT%H:%M:%S.%fZ")
        return [
            p
            for p in producers
            if p.get("lastPublicationDate")
            and datetime.strptime(p["lastPublicationDate"], "%Y-%m-%dT%H:%M:%S.%fZ")
            > filter_date
        ]
    except ValueError:
        click.echo(
            click.style("Invalid date format. Use YYYY-MM-DDThh:mm:ss.000Z", fg="red"),
            err=True,
        )
        return producers


def check_lcd_behind(
    producers: List[Dict], hours: int, email: str = None
) -> List[Dict]:
    """Check if any producers are behind by specified hours"""
    if not hours:
        return producers

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=hours)

    behind_producers = [
        p
        for p in producers
        if p.get("lastPublicationDate")
        and datetime.strptime(
            p["lastPublicationDate"], "%Y-%m-%dT%H:%M:%S.%fZ"
        ).replace(tzinfo=timezone.utc)
        < cutoff
    ]

    if behind_producers and email:
        send_email_alert(email, behind_producers, hours)

    return behind_producers


def send_email_alert(email_address: str, producers: List[Dict], hours: int):
    """Send email alert for producers that are behind"""
    if "," in email_address:
        recipients = email_address.split(",")
    else:
        recipients = [email_address]

    try:
        from email.mime.text import MIMEText

        # Generate report body
        report = "The following producers are behind:\n\n"
        for p in producers:
            report += f"Producer: {p['name']}\n"
            report += f"Last Publication Date: {p['lastPublicationDate']}\n"
            report += f"Source URL: {p['serviceRootUrl']}\n"
            report += f"[WARNING! LCD threshold exceeded ({hours} hours)]\n\n"

        # Send to each recipient
        for recipient in recipients:
            msg = MIMEText(report)
            msg["Subject"] = (
                f"GSS Producer Alert: {len(producers)} producers behind by {hours} hours"
            )
            msg["From"] = recipient
            msg["To"] = recipient

            click.echo("Working on sending email alert...")
            s = smtplib.SMTP("localhost")
            s.sendmail(msg["From"], msg["To"], msg.as_string())
            s.quit()

    except Exception as e:
        click.echo(click.style(f"Failed to send email alert: {e}", fg="red"), err=True)
        raise


@click.command()
@click.option(
    "-l",
    "--local-config",
    "local_config",
    type=str,
    required=True,
    help="Local GSS instance configuration file",
)
@click.option(
    "-s",
    "--filter-string",
    "filter_string",
    type=str,
    help="Filter string to match against producer filters",
)
@click.option(
    "-t",
    "--hours-behind",
    "hours_behind",
    type=int,
    help="Number of hours LCD can be behind current time",
)
@click.option(
    "-e",
    "--email",
    "email",
    type=str,
    help="Email address for notifications when using -t option",
)
def main(local_config, filter_string, hours_behind, email):
    """List producers and consumers from GSS instance"""
    config = configparser.ConfigParser()
    if not config.read(local_config):
        click.echo(
            click.style(f"Could not read config file: {local_config}", fg="red"),
            err=True,
        )
        return

    base_url = config["default"].get("serviceRootUrl")
    if not base_url:
        click.echo(
            click.style("No 'serviceRootUrl' found in config file", fg="red"), err=True
        )
        return

    producers = get_producers(base_url)
    consumers = get_consumers(base_url)

    if not producers and not consumers:
        click.echo("No producers or consumers found")
        return

    # Apply filters
    if filter_string:
        producers = filter_by_string(producers, filter_string)

    if hours_behind:
        producers = check_lcd_behind(producers, hours_behind, email)

    if not producers:
        click.echo(
            click.style("No producers found after applying filters", fg="yellow")
        )
        return

    if email and not hours_behind:
        click.echo(
            click.style(
                "Email option (-e) can only be used with hours-behind option (-t)",
                fg="yellow",
            )
        )

    consumer_lookup = (
        {c["name"].replace("-consumer", ""): c for c in consumers} if consumers else {}
    )

    headers = [
        "Producer Name",
        "Consumer Name",
        "Source URL",
        "GSS Instance",
        "Last Creation Date",
        "Filter",
    ]

    table_data = format_table_data(producers, consumer_lookup)

    click.echo(
        "\n"
        + tabulate(
            table_data,
            headers=headers,
            tablefmt="grid",
            colalign=("left", "left", "left", "left", "left", "left"),
        )
    )


if __name__ == "__main__":
    main()
