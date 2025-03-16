tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")


def  listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task # {index + 1}. {task}\n")


def deleteTask():

    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete:")) - 1
        if taskToDelete <=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task # {taskToDelete} has been removed ")
        else:
            print(f"Task # {taskToDelete} does not exist")

    except:
        print("Invalid input.")
        
def editTask():
    listTasks()
    if len(tasks) == 0:
        return
    try:
        taskToEdit = int(input("What task would you like to edit? ")) - 1 #taskToEdit = THE NUMBER OF THE TASK TO EDIT
        if taskToEdit <=0 and taskToEdit < len(tasks):
            edit = input("What would you want to edit the task to?") # edit = WHAT WE CHANGE THE TASK TO
            tasks[taskToEdit] = edit
            print(f"Task # {taskToEdit} has been changed to {edit}")
        else:
            print(f"Task # {taskToEdit} does not exist")

    except:
        print("Invalid input.")
            
if  __name__  == "__main__":
    ### Create a loop  
    print("Welcome to the to-do list app:")
    
    while True:
        ### Ask the user for a task
        print("\n")
        print("Please select one of the following options:") 
        print("-------------------------------------------") 
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Edit task")
        print("5. Quit")
        
        choice = input("\nEnter your choice: ")
        if(choice == "1"):
            addTask()        
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            editTask()
        elif(choice == "5"):
            break
        else:
            print("Invalid input. Please try again.")
            
    print("\nGoodbye👋👋")