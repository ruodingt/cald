import click
from caldiff.date import calendar_date_diff_str


@click.command(help="This CLI tool helps you calculate the unsigned differences (in number of days) "
                    "between date1 and date2")
@click.option('--date1', help="input you first date", default='2022-02-03', prompt=True)
@click.option('--date2', help="Add a thematic break", default='2022-01-25', prompt=True)
def cald(date1: str, date2: str):
    """
    This CLI tool helps you calculate the unsigned differences (in number of days)
    @param date1:
    @param date2:
    @return: None
    """
    diff = calendar_date_diff_str(date1, date2, signed=False)
    print(f"the difference is {diff} days")
