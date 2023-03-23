import PySimpleGUI as sg

def read_inputs(values):
    first_name = values["FIRST_NAME"]
    last_name = values["LAST_NAME"]
    date_of_birth = values["DATE_OF_BIRTH"]
    height = values["HEIGHT"]
    weight = values["WEIGHT"]
    is_taking_medication = values["IS_TAKING_MEDICATION"]
    print(first_name)
    print(last_name)
    print(date_of_birth)
    print(height)
    print(weight)
    print(is_taking_medication)

def create_layout():
    return [
        [sg.Text('First name'),sg.Input(key="FIRST_NAME")],
        [sg.Text('Last name'),sg.Input(key="LAST_NAME")],
        [sg.Text('Date of birth'),sg.Input(key="DATE_OF_BIRTH"),sg.CalendarButton('Select date')],
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
    patient_intake_window.close()