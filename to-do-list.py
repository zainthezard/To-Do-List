tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
        
if  __name__  == "__main__":
    ### Create a loop  
    print("Welcome to the to-do list app:")
    
    while True:
        ### Ask the user for a task
        print("/n")
        print("Please select one of the following options:") 
        print("-------------------------------------------") 
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List Tasks")
        print("4. Quit") 
        
        choice = input("Enter your choice: ")
        if(choice == "1"):
            addTask()        
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTask()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")
            
    print("Goodbye👋👋")