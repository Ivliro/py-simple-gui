from patient import Patient
from datetime import datetime
import PySimpleGUI as sg

patients = [
    Patient("Miro","Krotky",datetime(1990,1,6),185,90.2,True),
    Patient("Janda","Kovacova",datetime(1995,7,10),165,60.2,False),
    Patient("Nimish","Narang",datetime(2000,12,12),191,80.2,True),
]

def convert_to_rows():
    new_list = []
    for patient in patients:
        new_list.append(patient.convert_to_list())
    return new_list

