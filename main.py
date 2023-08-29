
import click,json

@click.group()
def cli():
    pass

@cli.command()
@click.option("--desc", prompt="Enter the task Description", help="Enter the Description  of the task")
@click.option("--date", prompt="Enter the task Due Date", help="Enter the Due Date of the task")
def add(desc,date):  #Adding the task
   with open("todo.txt",'r') as file:
       data = file.read()
   my_dict = json.loads(data)
   index = my_dict['counter'] +1 # New index
   my_dict[index] = [desc,date]
   my_dict['counter'] = my_dict['counter'] +1
   print()
   with open("todo.txt","w") as file:
        file.write(json.dumps(my_dict,indent = index))
   print("Task Added Successfully")


@cli.command()
def show():
    with open("todo.txt",'r') as file:
       data = file.read()
    my_dict = json.loads(data)
    my_dict.pop("counter")
    print("-" * 20)
    for task_id,tasklist in my_dict.items():
        print(f"Task ID: {task_id}")
        print(f"Description: {tasklist[0]}")
        print(f"Due Date: {tasklist[1]}")
        print("-" * 20)


@cli.command()
@click.option("--taskid", prompt="Enter the task id to remove", help="Enter the task id to remove")
def complete(taskid):
    with open("todo.txt",'r') as file:
       data = file.read()
    my_dict = json.loads(data)
    task_removed = my_dict.pop(taskid) # particular task removed
    print(f"The tasked removed is : {task_removed}")
    my_dict['counter'] = my_dict['counter'] -1
    index = my_dict['counter']
    # counter = my_dict.pop("counter")  # to just decrement the taskid then will add
    # for key,value in my_dict:
    #     if key> taskid:
    with open("todo.txt","w") as file:
       file.write(json.dumps(my_dict,indent = index))

@cli.command()
@click.option("--taskid", prompt="Enter the task id to edit", help="Enter the task id to edit")
@click.option("--taskdesc", prompt="Enter the new task desc to edit", help="Enter the new task desc to edit")
@click.option("--taskdate", prompt="Enter the new task due date to edit", help="Enter the new task due date to edit")

def edit(taskid,taskdesc,taskdate):
    with open("todo.txt",'r') as file:
       data = file.read()
    my_dict = json.loads(data)

    try:
        # print(f"The details of {taskid} is as follows:")
        # print(my_dict[taskid])
        previous_info = my_dict[taskid][:]
        print(f"The previoun info is {previous_info}")
        index = my_dict['counter']
        my_dict[taskid][0] = taskdesc
        my_dict[taskid][1] = taskdate
        new_info = my_dict[taskid]
        print(f"The previous info was {previous_info} and the new info was {new_info}")

        with open("todo.txt",'w') as file:
            data = file.write(json.dumps(my_dict,indent=index))

    except Exception as e:
        error_message = str(e)
        print(f"The following exception took place {error_message}")
        print("One of the possible reasons for the error is the task id does not exist")

    
if __name__ == "__main__":
    try:
        file_name = "todo.txt"
        with open(file_name,'r') as file:
            pass
            #print(f'The {file_name} exist')

    except FileNotFoundError:
        # if file does not found, then need to create one 
        # and in that the counter variable and a dictioanry needs to be created
        print(f'The {file_name} does not exist, creating a one')

        with open(file_name,'w') as file:
            file.write("{\"counter\" : 0}")
            print(f'The {file_name} has been created and ready to do work')

    cli()
    