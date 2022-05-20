import unittest

from click.testing import CliRunner

from caldiff.cli import cald


class TestCaldCLI(unittest.TestCase):
    def test_cald(self):
        runner = CliRunner()
        result = runner.invoke(cald, ['--date1', '2021-03-01', '--date2', '2021-02-01'])
        assert result.exit_code == 0
