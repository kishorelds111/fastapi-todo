# Simple To-do List App

# This list will store all your tasks
todo_list = []

def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("✅ Task added!")

    elif choice == "2":
        if not todo_list:
            print("📭 No tasks found.")
        else:
            print("\n📋 Your Tasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")

    elif choice == "3":
        if not todo_list:
            print("📭 No tasks to delete.")
        else:
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
            try:
                del_index = int(input("Enter task number to delete: "))
                deleted = todo_list.pop(del_index - 1)
                print(f"❌ Deleted task: {deleted}")
            except (ValueError, IndexError):
                print("⚠️ Invalid input. Please try again.")

    elif choice == "4":
        print("👋 Exiting To-Do List. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Enter a number between 1 and 4.")
