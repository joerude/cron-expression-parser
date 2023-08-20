import unittest
from unittest.mock import patch
from io import StringIO
import sys

from main import main


class TestCronParserExampleScenario(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_example_scenario(self, mock_stdout):
        cron_expression = "*/15 0 1,15 * 1-5 /usr/bin/find"
        sys.argv = ["script_name.py", cron_expression]
        main()

        expected_output = (
            "minute         0 15 30 45\n"
            "hour           0\n"
            "day of month   1 15\n"
            "month          1 2 3 4 5 6 7 8 9 10 11 12\n"
            "day of week    1 2 3 4 5\n"
            "command /usr/bin/find\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_custom_scenario_1(self, mock_stdout):
        cron_expression = "0 12 1,15 * 3 /usr/bin/python"
        sys.argv = ["script_name.py", cron_expression]
        main()

        expected_output = (
            "minute         0\n"
            "hour           12\n"
            "day of month   1 15\n"
            "month          1 2 3 4 5 6 7 8 9 10 11 12\n"
            "day of week    3\n"
            "command /usr/bin/python\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_custom_scenario_2(self, mock_stdout):
        cron_expression = "*/30 9-17 2-7 5,6 1,4 /usr/bin/bash"
        sys.argv = ["script_name.py", cron_expression]
        main()

        expected_output = (
            "minute         0 30\n"
            "hour           9 10 11 12 13 14 15 16 17\n"
            "day of month   2 3 4 5 6 7\n"
            "month          5 6\n"
            "day of week    1 4\n"
            "command /usr/bin/bash\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_all_fields_wildcard(self, mock_stdout):
        cron_expression = "* * * * * /usr/bin/find"
        sys.argv = ["script_name.py", cron_expression]
        main()

        expected_output = (
            "minute         0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 "
            "33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59\n"
            "hour           0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\n"
            "day of month   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31\n"
            "month          1 2 3 4 5 6 7 8 9 10 11 12\n"
            "day of week    1 2 3 4 5 6 7\n"
            "command /usr/bin/find\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_no_command(self, mock_stdout):
        cron_expression = "*/10 5 15 * 1 /usr/bin/find"
        sys.argv = ["script_name.py", cron_expression]
        main()

        expected_output = (
            "minute         0 10 20 30 40 50\n"
            "hour           5\n"
            "day of month   15\n"
            "month          1 2 3 4 5 6 7 8 9 10 11 12\n"
            "day of week    1\n"
            "command /usr/bin/find\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
