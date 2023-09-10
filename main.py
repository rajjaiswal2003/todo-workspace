import click, json, datetime


@click.group()
def cli():
    pass


def is_valid_date(date_text):
    try:
        # Attempt to parse the date using the specified format (e.g., 'dd-mm-yyyy')
        datetime.datetime.strptime(date_text, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def display_task_list(test_mode=False):
    try:
        file_name = "test_todo.txt" if test_mode else "todo.txt"
        with open(file_name, "r") as file:
            data = file.read()
        my_dict = json.loads(data)
        my_dict.pop("counter")
        print("-" * 20)
        for task_id, tasklist in my_dict.items():
            print(f"Task ID: {task_id}")
            print(f"Description: {tasklist[0]}")
            print(f"Due Date: {tasklist[1]}")
            print("-" * 20)
    except FileNotFoundError:
        print("No tasks to show.")


@cli.command()
@click.option(
    "--desc",
    prompt="Enter the task Description",
    help="Enter the Description of the task",
)
@click.option(
    "--date", prompt="Enter the task Due Date", help="Enter the Due Date of the task"
)
@click.option("--test-mode", is_flag=True, help="Enable test mode")
def add(desc, date, test_mode=False):
    filename = "test_todo.txt" if test_mode else "todo.txt"

    if is_valid_date(date):
        with open(filename, "r") as file:
            data = file.read()

        my_dict = json.loads(data)
        index = my_dict["counter"] + 1
        my_dict[index] = [desc, date]
        my_dict["counter"] += 1

        with open(filename, "w") as file:
            file.write(json.dumps(my_dict, indent=4))
            print("Task Added Successfully")
    else:
        print("Invalid date format. Please enter a date in the 'dd-mm-yyyy' format.")


@cli.command()
@click.option("--test-mode", is_flag=True, help="Enable test mode")
def show(test_mode=False):
    filename = "test_todo.txt" if test_mode else "todo.txt"
    with open(filename, "r") as file:
        data = file.read()
    my_dict = json.loads(data)
    my_dict.pop("counter")
    print("-" * 20)
    for task_id, tasklist in my_dict.items():
        print(f"Task ID: {task_id}")
        print(f"Description: {tasklist[0]}")
        print(f"Due Date: {tasklist[1]}")
        print("-" * 20)


@cli.command()
@click.option("--test-mode", is_flag=True, help="Enable test mode")
def complete(test_mode=False):

    file_name = "test_todo.txt" if test_mode else "todo.txt"

    if test_mode:
        display_task_list(test_mode=True)
    else:
        display_task_list()

    with open(file_name, "r") as file:
        data = file.read()
    my_dict = json.loads(data)
    taskid = str(input("Enter the taskid to remove: "))
    if taskid in my_dict:
        task_removed = my_dict.pop(taskid)  # particular task removed
        print(f"The tasked removed is: {task_removed}")

        index = my_dict["counter"]
        with open(file_name, "w") as file:
            file.write(json.dumps(my_dict, indent=index))
    else:
        print(f"Task with ID {taskid} does not exist.")


@cli.command()
@click.option("--test-mode", is_flag=True, help="Enable test mode")
def edit(test_mode=False):
    filename = "test_todo.txt" if test_mode else "todo.txt"

    if test_mode:
        display_task_list(test_mode=True)
    else:
        display_task_list()

    with open(filename, "r") as file:
        data = file.read()
    my_dict = json.loads(data)
    taskid = str(input("Enter the taskid to edit :"))
    if taskid in my_dict:
        taskdesc = str(input("Enter the new task Description :"))
        taskdate = str(input("Enter the new task Due Date :"))
        try:

            previous_info = my_dict[taskid][:]
            print(f"The previous info is {previous_info}")

            my_dict[taskid][0] = taskdesc
            my_dict[taskid][1] = taskdate
            new_info = my_dict[taskid]
            print(
                f"The previous info was {previous_info} and the new info is {new_info}"
            )

            with open(filename, "w") as file:
                file.write(json.dumps(my_dict, indent=4))
            print(f"Task with ID {taskid} has been edited successfully.")

        except Exception as e:
            error_message = str(e)
            print(f"The following exception occurred: {error_message}")
            print(
                "One of the possible reasons for the error is that the task ID does not exist."
            )
    else:
        print(f"Task with ID {taskid} does not exist.")


if __name__ == "__main__":
    try:
        file_name = "todo.txt"
        with open(file_name, "r") as file:
            pass
            # print(f'The {file_name} exist')

    except FileNotFoundError:
        # if file does not found, then need to create one
        # and in that the counter variable and a dictioanry needs to be created
        print(f"The {file_name} does not exist, creating a one")

        with open(file_name, "w") as file:
            file.write('{"counter" : 0}')
            print(f"The {file_name} has been created and ready to do work")

    cli()
