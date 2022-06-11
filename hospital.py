class Hospital:
    def __init__(self, admin, doctor, nurses, department):
        self.admin = admin
        self.doctor = doctor
        self.nurses = nurses
        self.department = department

    def get_name(self):
        self.admin = input("Enter the name of the Admin :  ")
        self.doctor = input("Enter the name of the Doctor :  ")
        self.nurses = input("Enter the name of the Nurses :  ")
        self.department = input("Enter the Department name :  ")


class Department(Hospital):
    # def __init__(self, admin, doctor, nurses, department):
    #     self.admin = admin
    #     self.doctor = doctor
    #     self.nurses = nurses
    #     self.department = department

    def display_name(self):
        print("Name of admin : {}  Name of the Doctor  : {}  Name of the Nurses  :  {}  Name of the Department : {} \n"
              .format(self.admin, self.doctor, self.nurses, self.department))


class Patient:
    def __init__(self, name, age, department1, disease):
        self.name = name
        self.age = age
        self.department1 = department1
        self.disease = disease

    def get_name(self):
        print(" Enter the  Patient Details  :   \n")
        self.name = input("Enter the Name of the Patient :  ")
        self.age = input("Enter the Age of the Patient :  ")
        self.department1 = input("Enter the Department :  ")
        self.disease = input("Enter the Disease :  ")

    def display_name(self):
        print(" PATIENT DETAILS :  \n")
        print("Name of Patient : {} ".format(self.name))
        print("Patient Age : {} ".format(self.age))
        print("Patient: {} ".format(self.department1))
        print("name of the disease : {}\n".format(self.disease))


obj1 = Department("", "", "", "")
obj2 = Patient("", "", "", "")
obj1.get_name()
obj1.display_name()
obj2.get_name()
obj2.display_name()
