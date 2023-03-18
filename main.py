import PySimpleGUI as sg
import dataFunctions

table_headings = ["first name","last name","dob","height","weight","medicated?"]

table_data = dataFunctions.convert_to_rows()

#1
layout = [
    [sg.Table(headings=table_headings, values=table_data)]
]
#2
window = sg.Window('Patients\' list', layout)

#3
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
#4
window.close()

