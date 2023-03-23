import PySimpleGUI as sg
import dataFunctions

def read_inputs(values):
    first_name = values["FIRST_NAME"]
    last_name = values["LAST_NAME"]
    date_of_birth = values["DATE_OF_BIRTH"]
    height = values["HEIGHT"]
    weight = values["WEIGHT"]
    is_taking_medication = values["IS_TAKING_MEDICATION"]
    
    created_patient = dataFunctions.create_patient(first_name,last_name,date_of_birth,height,weight,is_taking_medication)
    #if created_patient

def create_layout():
    return [
        [sg.Text('First name'),sg.Input(key="FIRST_NAME")],
        [sg.Text('Last name'),sg.Input(key="LAST_NAME")],
        [sg.Text('Date of birth'),sg.Input(key="DATE_OF_BIRTH"),
         sg.CalendarButton('Select date', format='%Y/%m/%d')],
        [sg.Text('Height'),sg.Input(key="HEIGHT")],
        [sg.Text('Weight'),sg.Input(key="WEIGHT")],
        [sg.Text('Is taking medication?'),sg.Checkbox('Yes', key="IS_TAKING_MEDICATION")],
        [sg.Cancel(),sg.Button('Save')],
    ]

def display_intake_form():
    patient_intake_layout = create_layout()
    patient_intake_window = sg.Window('New patient form', patient_intake_layout)
    
    # display intake form window
    while True:
        event, values = patient_intake_window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Save':
            read_inputs(values)
            break
    patient_intake_window.close()