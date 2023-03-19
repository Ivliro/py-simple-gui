from datetime import datetime

class Patient():
    
    #dob = date of birth
    def __init__(self,first_name,last_name,dob,height,weight,is_medicated):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.height = height
        self.weight = weight
        self.is_medicated = is_medicated

    
    def convert_to_list(self):
        date_of_birth = datetime.strftime(self.dob, '%Y/%m/%d') # YYYY/MM/DD
        height = str(self.height)
        weight = str(self.weight)
        is_medicated = str(self.is_medicated)

        return [self.first_name, self.last_name, date_of_birth, height, weight, is_medicated]
    