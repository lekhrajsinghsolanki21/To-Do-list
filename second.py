
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Task '{removed}' deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n📋 To-Do List Menu:")
        print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == "4":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()