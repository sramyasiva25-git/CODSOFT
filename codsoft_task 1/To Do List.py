def show_menu():
    print("\n----- TO DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(task_list):
    task = input("Enter the task: ")
    task_list.append(task)
    print("Task added successfully!")

def view_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(task_list)):
            print(f"{i + 1}. {task_list[i]}")

def delete_task(task_list):
    view_tasks(task_list)
    if len(task_list) > 0:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(task_list):
            removed_task = task_list.pop(task_no - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")


def todo_list_app():
    tasks = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Exiting To-Do List. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

todo_list_app()