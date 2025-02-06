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


def format_producer_details(data: Dict) -> List[List[str]]:
    """Format producer JSON details into tabular format"""
    table_data = []

    def format_value(value):
        if isinstance(value, bool):
            return "✓" if value else "✗"
        elif value is None:
            return "N/A"
        return str(value)

    # Basic producer details
    basic_fields = [
        ("Name", data.get("name")),
        ("Kafka Hosts", data.get("hosts")),
        ("Topic", data.get("topic")),
        ("Push Interval", data.get("pushInterval")),
        ("Filter", data.get("filter")),
        ("Reprocess", data.get("reprocess")),
        ("Data Source", data.get("dataSource")),
    ]
    table_data.extend(basic_fields)

    # Process error details
    if "processError" in data:
        error = data["processError"]
        table_data.extend(
            [
                ("Process Error Active", format_value(error.get("active"))),
                ("Process Error Retries", error.get("retries")),
            ]
        )

    # Source configuration
    if "source" in data:
        source = data["source"]
        source_fields = [
            ("Source Type", source.get("sourceType")),
            ("Service Root URL", source.get("serviceRootUrl")),
            ("Top Results", source.get("top")),
            ("Last Publication Date", source.get("lastPublicationDate")),
            ("Source Filter", source.get("filter")),
            ("Source Type", source.get("type")),
            ("Assumed Format", source.get("assumedFormat")),
            ("Fetch Attributes", format_value(source.get("fetchAttributes"))),
            ("Fetch Quicklook", format_value(source.get("fetchQuicklook"))),
            ("Use Date From DB", format_value(source.get("useDateFromDb"))),
        ]
        table_data.extend(source_fields)

        # Auth details
        if "auth" in source:
            auth = source["auth"]
            auth_fields = [
                ("Auth Type", auth.get("type")),
                ("Client ID", auth.get("clientId")),
                ("Token Endpoint", auth.get("tokenEndpoint")),
            ]
            table_data.extend(auth_fields)

    return [[field, format_value(value)] for field, value in table_data]


def format_consumer_details(data: Dict) -> List[List[str]]:
    """Format consumer JSON details into tabular format"""
    table_data = []

    def format_value(value):
        if isinstance(value, bool):
            return "✓" if value else "✗"
        elif value is None:
            return "N/A"
        return str(value)

    # Basic consumer details
    basic_fields = [
        ("Name", data.get("name")),
        ("Parallel Ingests", data.get("parallelIngests")),
        ("Kafka Hosts", data.get("hosts")),
        ("Group ID", data.get("groupId")),
        ("Topics", data.get("topics")),
        ("Reprocess", format_value(data.get("reprocess"))),
        ("Poll Interval (ms)", data.get("pollIntervalMs")),
        ("Source Delete", format_value(data.get("sourceDelete"))),
        ("Ingest Threads", data.get("ingestThreads")),
        ("Temp Path", data.get("tmpPath")),
    ]
    table_data.extend(basic_fields)

    # Source configuration
    if "source" in data:
        source = data["source"]
        source_fields = [
            ("Source Type", source.get("sourceType")),
            ("Service Root URL", source.get("serviceRootUrl")),
            ("Source Type", source.get("type")),
            ("429 Retries", source.get("retriesOn429")),
            ("429 Retry Wait (ms)", source.get("retryWaitOn429Ms")),
        ]
        table_data.extend(source_fields)

        # Auth details
        if "auth" in source:
            auth = source["auth"]
            auth_fields = [
                ("Auth Type", auth.get("type")),
                ("Client ID", auth.get("clientId")),
                ("Token Endpoint", auth.get("tokenEndpoint")),
            ]
            table_data.extend(auth_fields)

    # Task list summary
    if "taskList" in data:
        for i, task in enumerate(data["taskList"], 1):
            task_fields = [
                (f"Task {i} Type", task.get("type", "").split(".")[-1]),
                (f"Task {i} Pattern", task.get("pattern")),
                (f"Task {i} Active", format_value(task.get("active"))),
                (f"Task {i} Stop on Failure", format_value(task.get("stopOnFailure"))),
                (f"Task {i} Try Limit", task.get("tryLimit")),
            ]
            if "targetStores" in task:
                task_fields.append((f"Task {i} Target Stores", task["targetStores"]))
            table_data.extend(task_fields)

    # Error manager details
    if "errorManager" in data:
        error_mgr = data["errorManager"]
        error_fields = [
            ("Error Location", error_mgr.get("errorLocation")),
            ("Error Manager Type", error_mgr.get("type")),
        ]
        table_data.extend(error_fields)

    return [[field, format_value(value)] for field, value in table_data]


def get_producer_details(base_url: str, name: str) -> Dict:
    """Get detailed information for a specific producer"""
    headers = {"accept": "application/json"}
    try:
        response = requests.get(f"{base_url}/producers/{name}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None


def get_consumer_details(base_url: str, name: str) -> Dict:
    """Get detailed information for a specific consumer"""
    headers = {"accept": "application/json"}
    try:
        response = requests.get(f"{base_url}/consumers/{name}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None


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
@click.option(
    "-f",
    "--full-details",
    "full_details",
    type=str,
    help="Show full JSON details for a specific producer name",
)
def main(local_config, filter_string, hours_behind, email, full_details):
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
            click.style("No 'serviceRootUrl' found in config file", fg="red"),
            err=True,
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

    if full_details:

        producer_details = get_producer_details(base_url, full_details)
        consumer_details = get_consumer_details(base_url, full_details)

        if producer_details:
            table_data = format_producer_details(producer_details)
            click.echo("\nProducer Details:")
            click.echo(
                tabulate(
                    table_data,
                    headers=["Field", "Value"],
                    tablefmt="grid",
                    colalign=("right", "left"),
                )
            )
            return

        elif consumer_details:
            table_data = format_consumer_details(consumer_details)
            click.echo("\nConsumer Details:")
            click.echo(
                tabulate(
                    table_data,
                    headers=["Field", "Value"],
                    tablefmt="grid",
                    colalign=("right", "left"),
                )
            )
            return
        else:
            click.echo(
                click.style(
                    f"No producer or consumer found with base name: {full_details}",
                    fg="red",
                ),
                err=True,
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

    # Display producer table
    producer_headers = [
        "Producer Name",
        "Consumer Name",
        "Source URL",
        "GSS Instance",
        "Last Creation Date",
        "Filter",
    ]
    producer_table = format_table_data(producers, consumer_lookup)

    click.echo("\nProducers:")
    click.echo(
        tabulate(
            producer_table,
            headers=producer_headers,
            tablefmt="grid",
            colalign=("left", "left", "left", "left", "left", "left"),
        )
    )


if __name__ == "__main__":
    main()
