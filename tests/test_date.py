import unittest

from caldiff.date import Date


class TestDate(unittest.TestCase):
    def test_date_from_string(self):
        d = Date.from_string("2000-12-01")
        assert d.year == 2000
        assert d.month == 12
        assert d.day == 1

        try:
            Date.from_string('2000')
        except Exception as e:
            assert type(e) == ValueError

    def test_eq(self):
        assert Date(2002, 12, 1) == Date(2002, 12, 1)

    def test_gt(self):
        assert Date(2002, 11, 2) > Date(2002, 11, 1)
        assert Date(2002, 12, 1) > Date(2002, 11, 1)
        assert Date(2003, 11, 1) > Date(2002, 11, 1)

        assert Date(2003, 11, 1) < Date(2004, 11, 1)
        assert Date(2003, 11, 1) < Date(2003, 12, 1)
        assert Date(2003, 11, 1) < Date(2003, 11, 2)

    def test_end_of_the_year(self):
        assert Date._end_of_the_year(year=1998) == Date(1998, 12, 31)

    def test_beginning_of_the_year(self):
        assert Date._beginning_of_the_year(year=1998) == Date(1998, 1, 1)

    def test_max_days_in_month(self):
        assert Date._max_days_in_month(year=2000, month=2) == 29
        assert Date._max_days_in_month(year=2004, month=2) == 29
        assert Date._max_days_in_month(year=1900, month=2) == 28

    def test_is_leap_year(self):
        assert Date.is_leap_year(year=2000) is True
        assert Date.is_leap_year(year=1900) is False
        assert Date.is_leap_year(year=4) is True
        assert Date.is_leap_year(year=2004) is True
        assert Date.is_leap_year(year=100) is False

    def test_diff(self):
        d1 = Date.from_string("2000-12-01")
        d2 = Date.from_string("2000-12-04")
        d3 = Date.from_string("2000-12-04")
        d4 = Date.from_string("2000-11-29")
        assert d2 - d1 == 3
        assert d1 - d2 == -3
        assert d2 - d3 == 0
        assert d4 - d3 == -5

    def test_repr(self):
        assert str(Date(1900, 2, 3)) == 'DATE[1900-2-3]'
