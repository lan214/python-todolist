import PySimpleGUI as sg

sg.theme("black")

label_feet = sg.Text("Enter feet:")
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter inches:")
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
result_label = sg.Text("", key="result")

exit_button = sg.Button("Exit")

window = sg.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inches, input_inches],
                                        [convert_button, result_label, exit_button]])


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


while True:
    event, values = window.read()
    match event:
        case "Convert":
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                result = convert(feet, inches)
                window["result"].update(value=f"{result} m", text_color="white")
            except ValueError:
                sg.popup("Please provide two numbers")
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
window.close()
