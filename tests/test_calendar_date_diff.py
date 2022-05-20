import unittest

from caldiff.date import calendar_date_diff_str


class TestDateDiffFunction(unittest.TestCase):
    def test_calendar_date_diff_business_logic(self):
        """
        Testing the actual business logic for calendar date differences
        @return:
        """
        assert calendar_date_diff_str("2000-12-01", "2000-12-04", signed=False) == 2
        assert calendar_date_diff_str("2001-1-3", "1999-3-5", signed=False) == 669
        assert calendar_date_diff_str("1999-3-5", "2001-1-3", signed=False) == 669
        assert calendar_date_diff_str("1999-3-5", "1999-3-4", signed=False) == 0
        assert calendar_date_diff_str("1999-3-5", "1999-3-5", signed=False) == 0
        assert calendar_date_diff_str("1999-3-5", "2020-1-3", signed=False) == 7608
