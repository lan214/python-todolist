import functions
import PySimpleGUI as sg

label = sg.Text("Enter a todo")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", size=(45, 10), enable_events=True)
edit_button = sg.Button("Edit")

window = sg.Window("My app",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(value['todo'] + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = value['todos'][0]
            new_todo = value['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            selected_todo = value['todos'][0][:-1]
            window['todo'].update(selected_todo)
        case sg.WINDOW_CLOSED:
            break
window.close()
