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

    if "add" in user_input:
        todo = user_input[4:] + "\n"
        with open(todos_filename, "r") as file:
            todos = file.readlines()
        todos.append(todo)
        with open(todos_filename, "w") as file:
            file.writelines(todos)
    if "show" in user_input:
        with open(todos_filename, "r") as file:
            todos = file.readlines()
        todos = [item.strip("\n") for item in todos]
        for index, todo in enumerate(todos):
            row = f"{index + 1}-{todo.capitalize()}"
            print(row)
    if "edit" in user_input:
        number = int(input("Enter the number you want to edit: "))
        number = number - 1
        new_todo = input("Enter the new value: ")

        with open(todos_filename, "r") as file:
            todos = file.readlines()

        todos[number] = new_todo + "\n"

        with open(todos_filename, "w") as file:
            file.writelines(todos)

    if "complete" in user_input:
        number = int(input("Enter the number you want to complete: "))
        with open(todos_filename, "r") as file:
            todos = file.readlines()
        removed_todo = todos.pop(number - 1).strip("\n")
        with open(todos_filename, "w") as file:
            file.writelines(todos)
        message = f"Todo {removed_todo} was marked as completed"
        print(message)
    if "exit" in user_input:
        break
print("Bye!")
