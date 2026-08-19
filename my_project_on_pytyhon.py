# Create an empty list to hold our tasks
tasks = []

def main():
    while True:
        print("\n=== To-Do List Application ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Completed")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ").strip()
        
        # 1. VIEW TASKS
        if choice == "1":
            if not tasks:
                print("\nNo tasks in your list.")
            else:
                print("\n--- Your Tasks ---")
                for index, task in enumerate(tasks, 1):
                    # Check the status to print a checkmark or empty space
                    status = "[x]" if task["completed"] else "[ ]"
                    print(f"{index}. {status} {task['name']}")

        # 2. ADD TASK
        elif choice == "2":
            task_name = input("\nEnter task name: ").strip()
            if task_name != "":
                # Add a simple dictionary into our list
                tasks.append({"name": task_name, "completed": False})
                print(f"Added: '{task_name}'")
            else:
                print("Task name cannot be empty.")

        # 3. MARK COMPLETED
        elif choice == "3":
            if not tasks:
                print("\nNo tasks to mark as completed.")
            else:
                print("\n--- Current Tasks ---")
                for index, task in enumerate(tasks, 1):
                    status = "[x]" if task["completed"] else "[ ]"
                    print(f"{index}. {status} {task['name']}")
                
                num = input("\nEnter the task number to mark completed: ")
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["completed"] = True
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a valid number.")

        # 4. DELETE TASK
        elif choice == "4":
            if not tasks:
                print("\nNo tasks to delete.")
            else:
                print("\n--- Current Tasks ---")
                for index, task in enumerate(tasks, 1):
                    status = "[x]" if task["completed"] else "[ ]"
                    print(f"{index}. {status} {task['name']}")
                
                num = input("\nEnter the task number to delete: ")
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Deleted task: '{removed['name']}'")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a valid number.")

        # 5. SEARCH TASK
        elif choice == "5":
            query = input("\nEnter keyword to search: ").strip().lower()
            found = False
            print(f"\n--- Search Results for '{query}' ---")
            for index, task in enumerate(tasks, 1):
                if query in task["name"].lower():
                    status = "[x]" if task["completed"] else "[ ]"
                    print(f"{index}. {status} {task['name']}")
                    found = True
            if not found:
                print("No matching tasks found.")

        # 6. EXIT
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose between 1 and 6.")

if _name_ == "_main_":
    main()# Create an empty list to hold our tasks
tasks = []

def main():
    while True:
        print("\n=== To-Do List Application ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Completed")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ").strip()
        
        # 1. VIEW TASKS
        if choice == "1":
            if not tasks:
                print("\nNo tasks in your list.")
            else:
                print("\n--- Your Tasks ---")
                for index, task in enumerate(tasks, 1):
                    # Check the status to print a checkmark or empty space
                    status = "[x]" if task["completed"] else "[ ]"
                    print(f"{index}. {status} {task['name']}")

        # 2. ADD TASK
        elif choice == "2":
            task_name = input("\nEnter task name: ").strip()
            if task_name != "":
                # Add a simple dictionary into our list
                tasks.append({"name": task_name, "completed": False})
                print(f"Added: '{task_name}'")
            else:
                print("Task name cannot be empty.")

        # 3. MARK COMPLETED
        elif choice == "3":
            if not tasks:
                print("\nNo tasks to mark as completed.")
            else:
                print("\n--- Current Tasks ---")
                for index, task in enumerate(tasks, 1):
                    status = "[x]" if task["completed"] else "[ ]"
                    print(f"{index}. {status} {task['name']}")
                
                num = input("\nEnter the task number to mark completed: ")
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["completed"] = True
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a valid number.")

        # 4. DELETE TASK
        elif choice == "4":
            if not tasks:
                print("\nNo tasks to delete.")
            else:
                print("\n--- Current Tasks ---")
                for index, task in enumerate(tasks, 1):
                    status = "[x]" if task["completed"] else "[ ]"
                    print(f"{index}. {status} {task['name']}")
                
                num = input("\nEnter the task number to delete: ")
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Deleted task: '{removed['name']}'")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a valid number.")

        # 5. SEARCH TASK
        elif choice == "5":
            query = input("\nEnter keyword to search: ").strip().lower()
            found = False
            print(f"\n--- Search Results for '{query}' ---")
            for index, task in enumerate(tasks, 1):
                if query in task["name"].lower():
                    status = "[x]" if task["completed"] else "[ ]"
                    print(f"{index}. {status} {task['name']}")
                    found = True
            if not found:
                print("No matching tasks found.")

        # 6. EXIT
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose between 1 and 6.")
main()

