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


if __name__ == "__main__":
    unittest.main()
