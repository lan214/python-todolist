import functions
import PySimpleGUI as sg

label = sg.Text("Enter a todo")
input_box = sg.Input(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My app", layout=[[label], [input_box, add_button]])
window.read()
window.close()
