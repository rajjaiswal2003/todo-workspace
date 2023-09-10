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

    def test_edit_task(self):

        # Simulate user input
        user_input = "1\nNew Task Description\n2023-09-20\n"
        stdin_mock = StringIO(user_input)

        with open("test_todo.txt", "w") as file:
            file.write('{"counter": 1, "1": ["Test Task", "01-01-2023"]}')

        with patch("builtins.input", side_effect=user_input.split("\n")):
            result = self.runner.invoke(edit, ["--test-mode"])

        self.assertEqual(result.exit_code, 0)
        print(result.output)  # Print the output of the complete command
        print("EDITING OF TASK FUNCTIONALITY CHECKED \n")


if __name__ == "__main__":
    unittest.main()
