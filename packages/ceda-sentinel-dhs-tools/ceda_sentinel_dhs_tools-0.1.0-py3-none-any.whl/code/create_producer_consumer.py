import requests
import click
import json
import configparser
from jinja2 import Template
from datetime import datetime, timezone
from pathlib import Path


def validate_date_format(date_string):
    """Validate date string is in correct ISO format"""
    try:
        datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        return True
    except ValueError:
        return False


def get_template_paths(base_name: str) -> tuple[str, str]:
    """Get producer and consumer template paths from base name"""
    template_dir = Path(__file__).parent.parent / "templates"

    # Find template files
    producer_template = template_dir / f"{base_name}_producer.json"
    consumer_template = template_dir / f"{base_name}_consumer.json"

    if not producer_template.exists():
        raise ValueError(f"Producer template not found: {producer_template}")
    if not consumer_template.exists():
        raise ValueError(f"Consumer template not found: {consumer_template}")

    return str(producer_template), str(consumer_template)


def create_producer_consumer(
    base_url, template_base, config_file, filter_string=None, last_publication_date=None
):
    """Create a new producer using the provided template and config"""

    headers = {"accept": "application/json", "Content-Type": "application/json"}

    try:
        # Get templates
        producer_template, consumer_template = get_template_paths(template_base)

        # Load config
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(config_file)

        if "default" not in config:
            raise ValueError(
                f"No 'default' section found in config file: {config_file}"
            )

        config_dict = dict(config["default"])

        # Validate required names
        if not config_dict.get("base_name"):
            raise ValueError("base_name is missing in config file")

        # Add filter (required) - Wrap in quotes for JSON
        config_dict["filter"] = (
            f'"{filter_string} and PublicationDate lt {last_publication_date}"'
        )

        # Add last publication date
        if last_publication_date:
            if not validate_date_format(last_publication_date):
                raise ValueError(
                    "Last publication date must be in format: YYYY-MM-DDThh:mm:ss.000Z"
                )
            config_dict["lastPublicationDate"] = last_publication_date
        else:
            config_dict["lastPublicationDate"] = datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S.000Z"
            )

        # Create producer
        with open(producer_template, "r") as f:
            producer_template = Template(f.read())
        rendered = producer_template.render(**config_dict)
        producer_json = json.loads(rendered)

        response = requests.post(
            f"{base_url}/producers", headers=headers, json=producer_json
        )
        response.raise_for_status()
        producer_result = response.json()

        # Create consumer
        with open(consumer_template, "r") as f:
            consumer_template = Template(f.read())
        rendered = consumer_template.render(**config_dict)
        consumer_json = json.loads(rendered)

        response = requests.post(
            f"{base_url}/consumers", headers=headers, json=consumer_json
        )
        response.raise_for_status()
        consumer_result = response.json()

        return producer_result, consumer_result

    except Exception as e:
        if hasattr(e, "response"):
            error_json = e.response.json()
            error_message = error_json.get("message", "Unknown error")
            error_details = error_json.get("details", str(e))
            click.echo(
                click.style(
                    f"Message: {error_message}\nDetails: {error_details}", fg="red"
                ),
                err=True,
            )
        else:
            click.echo(click.style(f"Error: {str(e)}", fg="red"), err=True)
        return None, None


@click.command()
@click.option(
    "-t",
    "template_base",
    type=str,
    required=True,
    help="Base name for template files (e.g. 'colhub2_gss' for colhub2_gss_producer.json and colhub2_gss_consumer.json)",
)
@click.option(
    "-c",
    "config_file",
    type=str,
    required=True,
    help="Config file with credentials",
)
@click.option(
    "-l",
    "local_config",
    type=str,
    required=True,
    help="Local GSS instance configuration file",
)
@click.option(
    "-F",
    "filter_string",
    type=str,
    required=True,
    help="Filter string to apply to the producer name",
)
@click.option(
    "-L",
    "last_publication_date",
    type=str,
    help="Last publication date to apply to the producer",
)
def main(
    template_base, config_file, local_config, filter_string, last_publication_date
):
    """CEDA GSS Tools for creating producers

    This command creates a new producer using a template file and a config file.
    The local GSS instance configuration file is used to fetch the base URL of the
    GSS instance.

    Args:
        template_file (str): Template file for producer.
        config_file (str): Config file with credentials.
        local_config (str): Local GSS instance configuration file.
        filter_string (str): Filter string to apply to the producer name.
        last_publication_date (str): Last publication date to apply to the producer.
    """
    # Load local config
    config = configparser.ConfigParser()
    if not config.read(local_config):
        click.echo(
            click.style(f"Could not read config file: {local_config}", fg="red"),
            err=True,
        )
        return

    if "default" not in config:
        click.echo(
            click.style(
                f"No 'default' section found in config file: {local_config}", fg="red"
            ),
            err=True,
        )
        return

    base_url = config["default"].get("serviceRootUrl")
    if not base_url:
        click.echo(
            click.style("No 'serviceRootUrl' found in config file", fg="red"), err=True
        )
        return

    # Create producer/consumer pair
    producer_result, consumer_result = create_producer_consumer(
        base_url, template_base, config_file, filter_string, last_publication_date
    )

    if producer_result and consumer_result:
        click.echo(
            click.style("Producer/Consumer pair created successfully", fg="green")
        )
    else:
        click.echo(
            click.style("Error creating producer/consumer pair", fg="red"), err=True
        )


if __name__ == "__main__":
    main()
