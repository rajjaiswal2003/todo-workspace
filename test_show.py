import unittest
import os
from click.testing import CliRunner
from main import cli, add, show, edit, complete
from unittest.mock import patch, MagicMock
from io import StringIO
import json
import datetime


class TestToDoManager(unittest.TestCase):
    def setUp(self):
        self.test_data = {"counter": 0}
        with open("test_todo.txt", "w") as file:
            file.write(json.dumps(self.test_data))

        self.runner = CliRunner()

    def test_show(self):
        with open("test_todo.txt", "w") as file:
            file.write(
                '{"counter": 2, "1": ["Task 1", "2023-09-15"], "2": ["Task 2", "2023-09-20"]}'
            )

        # Debugging: Print content of test_todo.txt
        with open("test_todo.txt", "r") as file:
            print(file.read())

        result = self.runner.invoke(cli, ["show", "--test-mode"])
        print(result.output)  # Debugging: Print the output of the show command
        self.assertEqual(result.exit_code, 0)
        print("SHOWING OF TASK FUNCTIONALITY CHECKED \n")


if __name__ == "__main__":
    unittest.main()
