# def load_todos(filename="todos.txt"):
#     with open(filename, "r") as file:
#         todos = file.readlines()
#     return todos
#
#
# def write_todos(todos, filename="todos.txt"):
#     file = open("todos.txt", "w")
#     file.writelines(todos)
#     file.close()


while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip()
    todos_filename = "todos.txt"

    if user_input.startswith("add "):
        todo = user_input[4:] + "\n"
        with open(todos_filename, "r") as file:
            todos = file.readlines()
        todos.append(todo)
        with open(todos_filename, "w") as file:
            file.writelines(todos)
    elif user_input.startswith("show "):
        with open(todos_filename, "r") as file:
            todos = file.readlines()
        todos = [item.strip("\n") for item in todos]
        for index, todo in enumerate(todos):
            row = f"{index + 1}-{todo.capitalize()}"
            print(row)
    elif user_input.startswith("edit "):
        number = int(user_input[5:])
        number = number - 1
        new_todo = input("Enter the new value: ")

        with open(todos_filename, "r") as file:
            todos = file.readlines()

        todos[number] = new_todo + "\n"

        with open(todos_filename, "w") as file:
            file.writelines(todos)

    elif user_input.startswith("complete "):
        number = int(user_input[9:])
        with open(todos_filename, "r") as file:
            todos = file.readlines()
        removed_todo = todos.pop(number - 1).strip("\n")
        with open(todos_filename, "w") as file:
            file.writelines(todos)
        message = f"Todo {removed_todo} was marked as completed"
        print(message)
    elif "exit" in user_input:
        break
    else:
        print(f"Unknown command: {user_input}")
print("Bye!")
