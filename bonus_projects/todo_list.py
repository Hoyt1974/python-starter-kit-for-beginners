todos = []

while True:
    action = input("Add/View/Remove/Quit: ").lower()
    if action == "add":
        task = input("Enter task: ")
        todos.append(task)
    elif action == "view":
        print("To-Do List:")
        for i, task in enumerate(todos):
            print(f"{i + 1}. {task}")
    elif action == "remove":
        num = int(input("Task number to remove: "))
        if 0 < num <= len(todos):
            todos.pop(num - 1)
        else:
            print("Invalid number.")
    elif action == "quit":
        break
    else:
        print("Try again.")
