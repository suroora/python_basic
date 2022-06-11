class Computer:
    def __init__(self ,ram, storage, processor):
        self.processor = ram
        self.storage = storage
        self.ram = processor

    def getspace(self):
        print("Enter the specification ")
        self.ram = input("Enter the RAM in GB : ")
        self.storage = input("enter the storage space : ")
        self.processor = input("Enter the processor : ")

    def displayspec(self):
        print("Specifications of your system")
        print("Ram size : {} storage : {} Processor : {}".format(self.ram, self.storage, self.processor))


class Desktop(Computer):
    def __init__(self, model):
        self.model = model

    def get_model_name(self):
        self.model = input("Enter model name  of the computer : ")

    def show_model_name(self):
        print("Desktop specifications")
        print("model name : {}".format(self.model))


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        print("Laptop specifications")
        self.weight = input("Enter weight : ")

    def show_weight(self):
        print("Laptop weight : {}".format(self.weight))


object1 = Laptop("")
object2=Desktop("")
object1.getspace()
object1.displayspec()
object2.get_model_name()
object2.show_model_name()
object1.get_weight()
object1.show_weight()
