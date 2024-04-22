import uuid


tasks_DB = {}
# print(type(tasks_DB))

def print_task(task_id) :
    try : 
        task = tasks_DB[task_id]
        print("\n----- Task -----")
        for key in task:
            print(key,":",task[key])
    
        print("\n\n")
        return True
    except : 
        print(f"\nTask Not Found with id `{task_id}` !!\nTry Again Later !\n\n")
        return False

def create_task() : 
    print("task creation starting.....")
    task_id = str(uuid.uuid4())
    # print(type(task_id))
    task_name = input("Enter task name : ")
    task_description = input("Enter task description : ")
    tasks_DB[task_id] = {
        "id" : task_id,
        "name" : task_name,
        "description" : task_description
    }
    print("\nTask is Created Successfully:")
    for key in tasks_DB[task_id]:
        print(key,":",tasks_DB[task_id][key])
    
    print("\n\n")

def show_task() :
    # print("task showing starting")
    task_id = input("Enter task id : ")
    print_task(task_id)

def delete_task() : 
    # print("delete task")
    task_id = input("Enter task id which you want to delete : ")
    try:
        tasks_DB.pop(task_id)
        print("\nTask is deleted, Successfully !!\n")
    except:
        print(f"\nTask with id {task_id} doesn't exist. Try Again Later with different id.\n")

def edit_task() :
    # print("edit task")
    task_id = input("Enter task id which you want to edit : ")

    print("Task Information which you want to edit : ")
    task = print_task(task_id)

    if(task):
        task_name = input("Enter new task name : ")
        task_description = input("Enter new task description : ")

        tasks_DB[task_id] = {
            "id" : task_id,
            "name" : task_name,
            "desciption" : task_description
        }

        print("Task Updated Successfully !")
    

def show_all_tasks() :
    # print("show all tasks")
    if(len(tasks_DB) == 0):
        print("\n No Task Exits. Please Create Some Task First :)\n\n")
    else:
        for task in tasks_DB:
            print_task(task)

def delete_all_tasks() :
    # print("delete all tasks")
    if(len(tasks_DB) == 0):
        print("\n No Task Exits. Please Create Some Task First :)\n\n")
    else:
        print(f"\nTotal {len(tasks_DB)} tasks deleted Successfully\n\n")
        tasks_DB.clear()







print("To-Do Application to manage your tasks")

start = True
while(start):

    print("\nTo Create a New Task Press 1")
    print("To Show a Task Press 2")
    print("To Edit a Task Press 3")
    print("To Delete a Task Press 4")
    print("To Show All Tasks Press 5")
    print("To Delete All Tasks Press 6")
    print("To Exit From Application Press 0")

    response = input("\nEnter what operations you want to do : ")

    try:
        response = int(response)
        
        if(response == 1) :
            create_task()
        elif(response == 2) :
            show_task()
        elif(response == 3) :
            edit_task()
        elif(response == 4) :
            delete_task()
        elif(response == 5) :
            show_all_tasks()
        elif(response == 6) :
            delete_all_tasks()
        elif(response == 0) :
            print("\n\nThank you for using our application.\n\n")
            break
        else :
            raise Exception("Not a valid input")
        
    except Exception as e:
        print(f"\n You entered {response}, which is not a vaild input.\n")