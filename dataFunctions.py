from patient import Patient
from datetime import datetime

patients = [
    Patient("Miro","Krotky",datetime(1990,1,6),185,90.2,True),
    Patient("Janda","Kovacova",datetime(1995,7,10),165,60.2,False),
    Patient("Nimish","Narang",datetime(2000,12,12),191,80.2,True),
]

def convert_to_rows():
    all_patients = []
    for patient in patients:
        all_patients.append(patient.convert_to_list())
    return all_patients

def create_patient(first_name,last_name,dob,height,weight,is_medicated):
    if len(first_name) < 2 or len(last_name) < 2 or dob == "" or height == "" or weight == "":
        return False
    # ak sa hocico pokazi, ideme do 'except' s chybou
    try:
        date_of_birth = datetime.strptime(dob, '%Y/%m/%d')
        # if is a future date of birth
        if date_of_birth > datetime.now():
            return False
        height = int(height)
        weight = float(weight)
        if height <= 0 or weight <= 0:
            return False
        #is_medicated = True if is_medicated == True else False

        patient = Patient(first_name,last_name,date_of_birth,height,weight,is_medicated)
        patients.append(patient)
        return True
    except:
        return False