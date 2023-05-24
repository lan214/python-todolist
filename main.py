def load_todos(filename="todos.txt"):
    file = open(filename, "r")
    todos = file.readlines()
    file.close()
    return todos


def write_todos(todos, filename="todos.txt"):
    file = open("todos.txt", "w")
    file.writelines(todos)
    file.close()


while True:
    action = input("Type add, show, edit, complete or exit: ")

    match action.strip():
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todos = load_todos()
            todos.append(todo)
            write_todos(todos)
        case "show" | "display":
            todos = load_todos()
            for index, todo in enumerate(todos):
                row = f"{index + 1}-{todo.capitalize()}"
                print(row)
        case "edit":
            number = int(input("Enter the number you want to edit: "))
            number = number - 1
            new_todo = input("Enter the new value: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter the number you want to complete: "))
            todos.pop(number - 1)
        case "exit":
            break
        case other_command:
            print("Command: " + other_command + " not recognized")
print("Bye!")
