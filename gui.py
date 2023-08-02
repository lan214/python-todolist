import functions
import PySimpleGUI as sg

label = sg.Text("Enter a todo")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My app",
                   layout=[[label], [input_box, add_button]],
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
        case sg.WINDOW_CLOSED:
            break
window.close()
