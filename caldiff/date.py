import re
from typing import Tuple, TypeVar

T = TypeVar('T')


class Date:
    """
    Class that represent a date (e.g. 1992-03-29) which could perform substract operation

    Example usage
    >>> Date.from_string('2001-12-4') - Date.from_string('2001-12-1')
    3
    >>> Date.from_string('2001-11-29') - Date.from_string('2001-12-1')
    -2
    """

    _max_days_in_month_dic = {
        1: 31,
        2: 28,
        '2l': 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    _DAYS_PER_YEAR_REG = 365
    _DAYS_PER_YEAR_LEAP = 366

    def __init__(self, year: int, month: int, day: int):
        """
        Init an Date object
        :param year:
        :param month:
        :param day:
        """
        assert year >= 0, "year must be equal to or greater than 0"
        self.year: int = year
        self.month: int = month
        self.day: int = day
        self._validate_date()

    def __repr__(self):
        return f"DATE[{self.year}-{self.month}-{self.day}]"

    __str__ = __repr__

    @classmethod
    def from_string(cls, date_string: str) -> "Date":
        """
        Construct a Date object from a formatted string (e.g. 2021-06-08)

        @param date_string:
        @return:

        @raise ValueError: on mal-formatted input string
        """
        pattern_discover = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_string)
        if pattern_discover:
            y, m, d = pattern_discover.groups()
            return Date(year=int(y), month=int(m), day=int(d))
        else:
            raise ValueError(f"Your input `{date_string}` is not a valid date string. "
                             f"Expecting strings like 'yyyy-mm-dd' e.g.(2021-02-03)")

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Identify whether a year is a leap year
        @param year:
        @return:
        """
        _can_div_by_4 = year % 4 == 0
        _can_div_by_100 = year % 100 == 0
        _can_div_by_400 = year % 400 == 0

        if _can_div_by_4 and not _can_div_by_100:
            return True
        elif _can_div_by_400:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        if self.year > other.year:
            return True
        elif self.year == other.year and self.month > other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day > other.day:
            return True

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __eq__(self, other) -> bool:
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __sub__(self, other: "Date") -> int:
        """
        Calculate the diff (in number of days) between two dates
        @param other: another Date object
        @return: signed difference
        """

        _sign, d1, d2 = _rearrange(self, other)

        total_days_diff = 0

        if d1.year == d2.year:
            if d1.month == d2.month:
                return (d2.day - d1.day) * _sign

            # count days from d1 TO end of current d1 month
            total_days_diff += self._max_days_in_month(year=d1.year, month=d1.month) - d1.day

            # count days in whole months in between
            for mon in range(d1.month + 1, d2.month):
                total_days_diff += self._max_days_in_month(year=d1.year, month=mon)

            # count days from beginning of d2.month
            total_days_diff += d2.day
        else:
            # count days from d1 TO end of current d1 month
            total_days_diff += self._end_of_the_year(year=d1.year) - d1

            # count days in the whole years in the middle
            for y_ in range(d1.year + 1, d2.year):
                total_days_diff += self._DAYS_PER_YEAR_LEAP if self.is_leap_year(y_) else self._DAYS_PER_YEAR_REG

            # count days from beginning of the year d2.year to d2 (including the first day in d2.year)
            total_days_diff += d2 - self._beginning_of_the_year(year=d2.year) + 1

        return total_days_diff * _sign

    @classmethod
    def _end_of_the_year(cls, year) -> "Date":
        """
        Get the last day of the year
        @param year:
        @return:
        """
        _last_month = 12
        return Date(year=year, month=_last_month, day=cls._max_days_in_month_dic[_last_month])

    @classmethod
    def _beginning_of_the_year(cls, year) -> "Date":
        _first_month = 1
        return Date(year=year, month=_first_month, day=1)

    def _validate_date(self):
        """
        Make sure the date is valid date
        @return: None

        @raise AssertionError: On invalid date components (year, month, day)
        """
        assert self.year >= 0, "year must be equal to or greater than"
        assert 1 <= self.month <= 12, "month must be within the range [1,12]"
        _max_days = self._max_days_in_month(year=self.year, month=self.month)
        assert 1 <= self.day <= _max_days, f"month must be within the range [1,{_max_days}] in {self.year}-{self.month}"

    @classmethod
    def _max_days_in_month(cls, year: int, month: int) -> int:
        """
        Get max days in a certain month given the specified month & year
        @param year:
        @param month:
        @return:
        """
        m = month
        if month == 2:
            if cls.is_leap_year(year):
                m = '2l'
        return cls._max_days_in_month_dic[m]


def _rearrange(a: T, b: T) -> Tuple[int, T, T]:
    """
    range arrange the order of a, b and produce the sign (1 or -1)
    if a >= b, the function will return 1, b, a
    otherwise (b>a) , return -1, a, b

    @param a:
    @param b:
    @return: A tuple (Integer, T1, T2), where T2 >= T1 guaranteed
    """
    if a >= b:
        _sign = 1
        d1 = b
        d2 = a
    else:
        _sign = -1
        d1 = a
        d2 = b

    return _sign, d1, d2


def _calendar_date_diff(d1: Date, d2: Date, signed=False) -> int:
    """
    Calendar date difference calculate business logic:
        if unsigned:
            abs(d1-d2) -1

    @param signed: whether to produce signed difference
    @param d1: Date object
    @param d2: Date object
    @return: An integer, specify the difference (in number of days) of two dates (d1-d2-1)
    """

    sign = 1
    if d1 == d2:
        diff: int = 0
    elif d1 < d2:
        diff: int = d2 - d1 - 1
        sign = -1
    else:
        diff: int = d1 - d2 - 1

    return sign * diff if signed else diff


def calendar_date_diff_str(d1: str, d2: str, signed: False) -> int:
    """
    Calendar date difference calculate business logic.

    @param d1: formatted string for date, e.g 2021-09-08
    @param d2:
    @param signed:
    @return: None
    """
    d1 = Date.from_string(d1)
    d2 = Date.from_string(d2)
    return _calendar_date_diff(d1=d1, d2=d2, signed=signed)


if __name__ == "__main__":
    print(calendar_date_diff_str(d1="1992-12-17", d2="1992-12-10", signed=True))
