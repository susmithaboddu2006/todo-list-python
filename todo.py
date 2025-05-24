import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['title']}")
        print()

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.\n")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
