import unittest

from caldiff.date import calendar_date_diff_str


class TestDateDiffFunction(unittest.TestCase):
    def test_calendar_date_diff_business_logic(self):
        """
        Testing the actual business logic for calendar date differences
        @return:
        """
        assert calendar_date_diff_str("2000-12-01", "2000-12-04", signed=False) == 2
        assert calendar_date_diff_str("2001-01-03", "1999-03-05", signed=False) == 669
        assert calendar_date_diff_str("1999-03-05", "2001-01-03", signed=False) == 669
        assert calendar_date_diff_str("1999-03-05", "1999-03-04", signed=False) == 0
        assert calendar_date_diff_str("1999-03-05", "1999-03-05", signed=False) == 0
        assert calendar_date_diff_str("1999-03-05", "2020-01-03", signed=False) == 7608
