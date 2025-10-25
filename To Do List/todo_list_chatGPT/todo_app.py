class ToDoApp:
    """
    A simple To-Do List class that manages user tasks.
    """

    def __init__(self):
        """Initialize the ToDoApp with an empty task list."""
        self.tasks = []

    def add_task(self):
        """
        Add a new task entered by the user to the list.
        """
        task = input("Enter your task: ")
        self.tasks.append(task)
        print("✅ Task added successfully!")

    def view_tasks(self):
        """
        Display all tasks in the current list.
        """
        if not self.tasks:
            print("📭 No tasks to show.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
            print()

    def remove_task(self):
        """
        Remove a specific task from the list.
        """
        if not self.tasks:
            print("📭 No tasks to remove.")
            return

        rm_task = input("Enter the task to remove: ")
        if rm_task in self.tasks:
            self.tasks.remove(rm_task)
            print("🗑️ Task removed successfully!")
        else:
            print("❌ Task not found in your list.")

    def handle_action(self, action):
        """
        Handle a user command and call the proper method.
        """
        if action == "add":
            self.add_task()
        elif action == "view":
            self.view_tasks()
        elif action == "remove":
            self.remove_task()
        elif action == "exit":
            print("👋 Goodbye! Have a productive day.")
            return False
        else:
            print("⚠️ Invalid command. Please try again.")
        return True

    def run(self):
        """
        Run the To-Do List application loop.
        """
        print("📝 Welcome to the To-Do List App!")
        while True:
            action = input("Choose a command (add, view, remove, exit): ").strip().lower()
            if not self.handle_action(action):
                break
