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

    def test_complete(self):
        user_input = "1\n"  # Simulate user input for task ID
        stdin_mock = StringIO(user_input)

        # Create a test_todo.txt file with some tasks
        with open("test_todo.txt", "w") as file:
            file.write(
                '{"counter": 2, "1": ["Task 1", "2023-09-15"], "2": ["Task 2", "2023-09-20"]}'
            )

        with patch("builtins.input", side_effect=user_input):
            result = self.runner.invoke(complete, ["--test-mode"])

        self.assertEqual(result.exit_code, 0)
        print(result.output)  # Print the output of the complete command
        print("COMPLETION OF TASK FUNCTIONALITY CHECKED \n")

    def test_complete_with_nonexistent_task(self):
        user_input = "3\n"  # Simulate user input for task ID
        stdin_mock = StringIO(user_input)

        with open("test_todo.txt", "w") as file:
            file.write(
                '{"counter": 2, "1": ["Task 1", "2023-09-15"], "2": ["Task 2", "2023-09-20"]}'
            )

        with patch("builtins.input", side_effect=user_input):
            result = self.runner.invoke(complete, ["--test-mode"])

        self.assertEqual(result.exit_code, 0)
        print(result.output)  # Print the output of the complete command
        print("COMPLETION OF TASK WITH NON EXISTENCE OF ID FUNCTIONALITY CHECKED \n")


if __name__ == "__main__":
    unittest.main()
