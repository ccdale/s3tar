"""s3tar main module.

entry point: star()
"""
import click


@click.group()
def cli():
    pass


urlhelp = "A full 's3://<bucket>/prefix/prefix' type path"


@cli.command()
@click.option(
    "-b", "--bucket", type=click.STRING, help="bucket name (i.e. sniffer-logs)"
)
@click.option("-e", "--end", type=click.STRING, help="optional end time")
@click.option(
    "-l", "--length", type=click.STRING, help="optional time length (i.e. 1d, 3h, 4w)"
)
@click.option(
    "-p",
    "--prefix",
    type=click.STRING,
    help="prefix (i.e. 'prefix/sub-dir/sub-sub-dir')",
)
@click.option(
    "-P", "--profile", type=click.STRING, help="AWS CLI profile to use (chaim alias)"
)
@click.option("-s", "--start", type=click.STRING, help="optional start time")
@click.option(
    "-u",
    "--url",
    type=click.STRING,
    help="A full 's3://<bucket>/prefix/prefix' type path",
)
def star(bucket, end, length, prefix, start, url):
    """Generates a tar archive of S3 files.

    Files are selected by prefix and optionaly by a time-based filter.

    You can select files via the full 's3://<bucket>/prefix/sub-dir' type
    path, or pass seperate options for the bucket name and prefix.
    A leading slash will be added to the prefix if it is missing.
    A trailing slash will be added to the prefix if it is missing and time
    based filtering is used.

    if 'url' is given both 'bucket' and 'prefix' are ignored if also given.

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
    performed, and all files from the prefix downwards are copied across
    to the tar archive recursively.
    """
    pass
