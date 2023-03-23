import PySimpleGUI as sg
import dataFunctions
import patientIntakeForm

table_headings = ["first name","last name","dob","height","weight","medicated?"]

table_data = dataFunctions.convert_to_rows()

def press_add_button(patients_window):
    patientIntakeForm.display_intake_form()
    table_data = dataFunctions.convert_to_rows()
    patients_window["PATIENTS_TABLE"].update(values=table_data)


# patients window stuff
patients_window_layout = [
    [sg.Text('All patients data'), sg.Button('Add new patient')],
    [sg.Table(headings=table_headings, values=table_data, key="PATIENTS_TABLE")]
]
patients_window = sg.Window('Patients\' list', patients_window_layout)

# display patient window
while True:
    event, values = patients_window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Add new patient':
        press_add_button(patients_window)
patients_window.close()

