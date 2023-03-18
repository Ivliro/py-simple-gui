from patient import Patient
from datetime import datetime
import PySimpleGUI as sg

patients = [
    Patient("Miro","Krotky",datetime(1990,1,6),185,90.2,True),
    Patient("Janda","Kovacova",datetime(1995,7,10),165,60.2,False),
    Patient("Nimish","Narang",datetime(2000,12,12),191,80.2,True),
]

table_headings = ["first name","last name","dob","height","weight","medicated?"]

def convert_to_rows():
    all_patients = []
    for patient in patients:
        all_patients.append(patient.convert_to_list())
    return all_patients

#1
layout = [
    [sg.Table(headings=table_headings, values=convert_to_rows())]
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

