# ToDo List Manager

A simple command-line application to manage your tasks with descriptions and due dates.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

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

   
