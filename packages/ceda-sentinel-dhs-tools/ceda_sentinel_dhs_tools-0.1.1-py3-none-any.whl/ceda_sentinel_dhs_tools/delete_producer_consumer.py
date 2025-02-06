import requests
import click
import configparser


def delete_producer_consumer(base_url: str, base_name: str) -> bool:
    """Delete a producer/consumer pair using their base name"""
    headers = {"accept": "application/json"}

    try:
        # Delete producer
        producer_name = f"{base_name}-producer"
        producer_response = requests.delete(
            f"{base_url}/producers/{producer_name}", headers=headers
        )
        producer_response.raise_for_status()

        # Delete consumer
        consumer_name = f"{base_name}-consumer"
        consumer_response = requests.delete(
            f"{base_url}/consumers/{consumer_name}", headers=headers
        )
        consumer_response.raise_for_status()

        return True

    except requests.exceptions.HTTPError as e:
        if hasattr(e, "response") and e.response is not None:
            try:
                error_json = e.response.json()
                error_message = error_json.get("message", "Unknown error")
                error_details = error_json.get("details", str(e.response.text))
                click.echo(
                    click.style(
                        f"Error: {error_message}\nDetails: {error_details}", fg="red"
                    ),
                    err=True,
                )
            except:
                click.echo(click.style(f"Error: {str(e)}", fg="red"), err=True)
        else:
            click.echo(click.style(f"Error: {str(e)}", fg="red"), err=True)
        return False


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
    "-n",
    "--name",
    "base_name",
    type=str,
    required=True,
    help="Base name of producer/consumer pair to delete (without -producer/-consumer suffix)",
)
def main(local_config: str, base_name: str):
    """Delete a producer/consumer pair from GSS instance.

    This command deletes both the producer and consumer with the given base name
    from the GSS instance specified in the local configuration file.
    """
    # Load config
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

    # Delete producer/consumer pair
    if delete_producer_consumer(base_url, base_name):
        click.echo(
            click.style(
                f"Successfully deleted producer/consumer pair: {base_name}", fg="green"
            )
        )
    else:
        click.echo(
            click.style(
                f"Failed to delete producer/consumer pair: {base_name}", fg="red"
            ),
            err=True,
        )


if __name__ == "__main__":
    main()
