import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text("", key='clock')
label = sg.Text("Enter a todo")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", size=(45, 10), enable_events=True)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My app",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, value = window.read(timeout=33)
    window['clock'].update(value=time.strftime("%b %d, %Y - %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(value['todo'] + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select a todo first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Select a todo first", font=("Helvetica", 20))
        case "todos":
            selected_todo = value['todos'][0][:-1]
            window['todo'].update(selected_todo)
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
window.close()
