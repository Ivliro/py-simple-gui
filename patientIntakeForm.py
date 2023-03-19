import PySimpleGUI as sg


patient_intake_layout = [
    [sg.Text('First name'),sg.Input()],
    [sg.Text('Last name'),sg.Input()],
    [sg.Text('Date of birth'),sg.Input(),sg.CalendarButton('Select date')],
    [sg.Text('Height'),sg.Input()],
    [sg.Text('Weight'),sg.Input()],
    [sg.Text('Is taking medication?'),sg.Checkbox('Yes')],
    [sg.Cancel(),sg.Button('Save')],
]

def display_intake_form():
    patient_intake_window = sg.Window('New patient form', patient_intake_layout)
    
    # display intake form window
    while True:
        event, values = patient_intake_window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
    patient_intake_window.close()