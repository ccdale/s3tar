"""s3tar main module.

entry point: star()
"""
import click


@click.group()
def cli():
    pass


urlhelp = "A full 's3://<bucket>/prefix/prefix' type path"


@cli.command()
@click.option("-e", "--end", type=click.STRING, help="optional end time")
@click.option(
    "-l", "--length", type=click.STRING, help="optional time length (i.e. 1d, 3h, 4w)"
)
@click.option(
    "-p", "--profile", type=click.STRING, help="AWS CLI profile to use (chaim alias)"
)
@click.option("-s", "--start", type=click.STRING, help="optional start time")
@click.argument("path")
def star(start, end, length, profile, path):
    """Generates a tar archive of S3 files.

    Files are selected by a path made up of 'bucket/prefix'
    and optionaly by a time-based filter.

    'profile' is the AWS CLI profile to use for accessing S3.  If you use
    chaim or cca then this is the alias name for the account.

    The time based filter relies on the files being named with ISO Formatted
    dates and times embedded in the file names.  i.e.  'file_2020-03-04T12:32:21.txt'

    The 'start' and 'end' parameters can either be ISO formatted date strings
    or unix timestamps.  If only the date portion of the date/time string is given
    the time defaults to midnight of that day.

    The length parameter is a string of the form '3h', '2d', '1w' for,
    respectively 3 hours, 2 days or 1 week.  Only hours, days or weeks are
    supported.  The 'length' and 'end' parameters are mutually exclusive, give
    one or the other, not both.

    If neither the 'end' nor the 'length' parameter is given, the end time
    defaults to 'now'.

    If the 'start' parameter is not given no filtering of the files is
    performed, and all files found down the path are copied across
    to the tar archive recursively.
    """
    pass
