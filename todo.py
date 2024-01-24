#!/usr/bin/python3 

def view_todo_list():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()

            if not tasks:
                print("To-Do List is empty.")
            else:
                print("To-Do List:")

                for id, task in enumerate(tasks, start=1):
                    print(f"{id}. {task.strip()}")

    except FileNotFoundError:
        print("To-Do List file not found. Creating a new one.")


def add_task():
    task = input("Enter the task: ")

    with open("todo.txt", "a") as file:
        file.write(task + "\n")

    print("Task added successfully!")


def mark_completed():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("To-Do List is empty.")
            return

        print("To-Do List:")
        for id, task in enumerate(tasks, start=1):
            print(f"{id}. {task.strip()}")
        
        task_index = int(input("Enter the task number to mark as completed: ")) - 1

        if 0 <= task_index < len(tasks):
            completed_task = tasks.pop(task_index)

            with open("completed.txt", "a") as completed_file:
                completed_file.write(completed_task)

            with open("todo.txt", "w") as file:
                file.writelines(tasks)

            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print("To-Do List file not found. Please add tasks first.")




def display_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Quit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Quitting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
