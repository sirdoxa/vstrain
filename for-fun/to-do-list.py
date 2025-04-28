tasks = []

def show_menu():
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def rm_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        rm_task()
    elif choice == '4':
        print("Goodluck ;)")
        break
    else:
        print("Invalid choice.")
