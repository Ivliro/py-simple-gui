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