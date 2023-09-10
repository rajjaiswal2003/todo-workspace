import unittest
import os
from click.testing import CliRunner
from main import cli, add, show, edit, complete
from unittest.mock import patch, MagicMock
from io import StringIO
import json


class TestToDoManager(unittest.TestCase):
    def setUp(self):
        self.test_data = {"counter": 0}
        with open("test_todo.txt", "w") as file:
            file.write(json.dumps(self.test_data))

        self.runner = CliRunner()

    def test_add_task(self):

        result = self.runner.invoke(
            cli, ["add", "--desc", "Task 1", "--date", "15-09-2023", "--test-mode"]
        )
        self.assertEqual(result.exit_code, 0)
        print(result.output)  # Print the output of the complete command
        print("ADDITION OF TASK FUNCTIONALIY CHECKED \n")

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
