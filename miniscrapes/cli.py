"""Console script for miniscrapes."""
import sys
import click

from miniscrapes.execution import run_scrapers


@click.group()
def main(args=None):
    pass


@main.command()
@click.option('--to', required=True, help='Miniscrape recipient email')
@click.option('--zip-code', required=True, help='Zipcode to scrape')
@click.option('--state', required=True, help='State to scrape')
def email_scrapers(to, zip_code, state):
    run_scrapers(to, zip_code, state)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
