import PySimpleGUI as sg

label_feet = sg.Text("Enter feet:")
input_feet = sg.Input()

label_inches = sg.Text("Enter inches:")
input_inches = sg.Input()

convert_button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inches, input_inches],
                                        [convert_button]])

window.read()
window.close()