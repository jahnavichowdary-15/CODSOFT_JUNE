import json
import os

TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Display all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print()

# Add a new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# Update an existing task
def update_task(tasks):
    list_tasks(tasks)
    index = int(input("Enter task number to update: ")) - 1
    if 0 <= index < len(tasks):
        new_task = input("Enter new task: ")
        tasks[index] = new_task
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    list_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Show menu
def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. List all tasks")
    print("2. Add a new task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if _name_ == "_main_":
    main()
