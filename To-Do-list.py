tasks = []
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully.")
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(f"Deleted task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Thank you for using the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")