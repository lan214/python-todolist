def get_todos():
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip()
    todos_filename = "todos.txt"

    if user_input.startswith("add "):
        todo = user_input[4:] + "\n"
        todos = get_todos()
        todos.append(todo)
        with open(todos_filename, "w") as file:
            file.writelines(todos)

    elif user_input.startswith("show"):
        todos = get_todos()
        todos = [item.strip("\n") for item in todos]
        for index, todo in enumerate(todos):
            row = f"{index + 1}-{todo.capitalize()}"
            print(row)

    elif user_input.startswith("edit "):
        try:
            number = int(user_input[5:])
            number = number - 1
            new_todo = input("Enter the new value: ")

            todos = get_todos()
            todos[number] = new_todo + "\n"

            with open(todos_filename, "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid command")

    elif user_input.startswith("complete "):
        try:
            number = int(user_input[9:])
            todos = get_todos()
            removed_todo = todos.pop(number - 1).strip("\n")
            with open(todos_filename, "w") as file:
                file.writelines(todos)
            message = f"Todo {removed_todo} was marked as completed"
            print(message)
        except IndexError:
            print("There is no value with that index")

    elif "exit" in user_input:
        break
        
    else:
        print(f"Unknown command: {user_input}")
print("Bye!")
