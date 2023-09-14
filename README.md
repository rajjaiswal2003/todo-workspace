# ToDo List Manager

A simple command-line application to manage your tasks with descriptions and due dates.


## Introduction

This command-line tool allows you to manage your to-do list efficiently. You can add, view, complete, and edit tasks with descriptions and due dates using simple commands.

## Features

- Add tasks with descriptions and due dates.
- View the list of tasks.
- Mark tasks as completed and remove them from the list.
- Edit task descriptions and due dates.

## Commands for doing operation in To-do Application


| Task                  | Parameters to Pass                     | Command                                                |
|-----------------------|----------------------------------------|--------------------------------------------------------|
| Creating a Task       | Description and Due Date               | `python main.py add --desc Description --date DueDate` |
| Showing List of Tasks | No Parameters                         | `python main.py show`                                 |
| Edit a Task           | Task ID, Task Description, Task Due Date | `python main.py edit --taskid TaskId --taskdesc TaskDescription --taskdate TaskDueDate` |
| Complete/Remove Task  | Task ID                                | `python main.py complete --taskid TaskID`              |


##  Testing and Code Quality:

This ToDo List Manager has been thoroughly tested to ensure its functionality. The following steps were taken to improve code quality:

- **Unit testing:** We've written unit tests for each functionality to ensure they work as expected.
- **Code linting:** We've used [Pylint](https://pylint.pycqa.org/) to maintain code consistency and adherence to coding standards.
- **Code formatting:** We've applied [Black](https://black.readthedocs.io/en/stable/) to make the code more readable and maintainable.


## Installation:

pip install -r requirements.txt
The requirements.txt file contains a list of all the dependencies needed to run the application.

## Continuous Integration with GitHub Actions
This project includes a GitHub Action workflow that automates the build and testing process. With this workflow, your code is tested for correctness and functionality every time a commit is pushed to the main branch.



   
