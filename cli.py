# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y - %H:%M:%S")
print("It is", now)

while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip()

    if user_input.startswith("add "):
        todo = user_input[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_input.startswith("show"):
        todos = functions.get_todos()
        todos = [item.strip("\n") for item in todos]
        for index, todo in enumerate(todos):
            row = f"{index + 1}-{todo.capitalize()}"
            print(row)

    elif user_input.startswith("edit "):
        try:
            number = int(user_input[5:])
            number = number - 1
            new_todo = input("Enter the new value: ")

            todos = functions.get_todos()
            todos[number] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Invalid command")

    elif user_input.startswith("complete "):
        try:
            number = int(user_input[9:])
            todos = functions.get_todos()
            removed_todo = todos.pop(number - 1).strip("\n")
            functions.write_todos(todos)
            message = f"Todo {removed_todo} was marked as completed"
            print(message)
        except IndexError:
            print("There is no value with that index")

    elif "exit" in user_input:
        break

    else:
        print(f"Unknown command: {user_input}")
print("Bye!")
