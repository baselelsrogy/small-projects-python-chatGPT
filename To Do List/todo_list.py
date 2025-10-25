print("Welcome to app (To Do List)")

toDoList = []

while True:
    user_action = input("Choice a command (add, view, remove, exit): ").strip().lower()

    if user_action == 'add':
        task = input("Enter your task: ")
        toDoList.append(task)
        print("Task was added")

    elif user_action == 'view':
        if not toDoList:
            print("No tasks to show")
        else:
            for task in toDoList:
                print(task)

    elif user_action == 'remove':
        if not toDoList:
            print("No tasks to remove")
        else:
            rm_task = input("What task you want to remove: ")
            if rm_task in toDoList:
                toDoList.remove(rm_task)
                print("Task removed")
            else: 
                print("Your task not found")

    elif user_action == 'exit':
        print("Goodbye!")
        break

    else:
        print("Invalid Command")
  