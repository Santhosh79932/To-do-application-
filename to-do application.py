import datetime

tasks = {}

def add_task():
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    due_date_str = input("Enter the due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks[task_name] = {"description": task_description, "due_date": due_date, "completed": False}
    print(f"Task '{task_name}' has been added.")

def display_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Task List:")
        for task_name, task_info in tasks.items():
            status = "Completed" if task_info["completed"] else "Not Completed"
            due_date = task_info["due_date"].strftime('%Y-%m-%d')
            print(f"{task_name}: {task_info['description']} (Due date: {due_date}) ({status})")

def mark_task_complete():
    task_name = input("Enter the name of the task you want to mark as complete: ")
    if task_name in tasks:
        tasks[task_name]["completed"] = True
        print(f"Task '{task_name}' has been marked as complete.")
    else:
        print(f"Task '{task_name}' not found in the task list.")

def update_task_description():
    task_name = input("Enter the name of the task you want to update: ")
    if task_name in tasks:
        new_description = input("Enter the new task description: ")
        tasks[task_name]["description"] = new_description
        print(f"Task '{task_name}' has been updated.")
    else:
        print(f"Task '{task_name}' not found in the task list.")

def remove_task():
    task_name = input("Enter the name of the task you want to remove: ")
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' has been removed.")
    else:
        print(f"Task '{task_name}' not found in the task list.")

while True:
    print("\nTask Management Menu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Complete")
    print("4. Update Task Description")
    print("5. Remove Task")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        update_task_description()
    elif choice == "5":
        remove_task()
    elif choice == "6":
        print('coded by santhosh')
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6).")
