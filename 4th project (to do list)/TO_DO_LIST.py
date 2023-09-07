class Task:
    def __init__(self, task_description, completed=False):
        self.task_description = task_description
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        task = Task(task_description)
        self.tasks.append(task)
        print("Task added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                status = " [X] " if task.completed else " [ ] "
                print(f"{i}. {status}{task.task_description}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Mark Task as Completed")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                task_description = input("Enter task description: ")
                self.add_task(task_description)
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                task_index = int(input("Enter task index to mark as completed: "))
                self.mark_completed(task_index)
            elif choice == "4":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
