class Student():
    def __init__(self, name, age, phone) -> None:
        self.name = name
        self.age = age
        self.phone = phone
    
    def getName(self):
        return self.name
    
    def changeName(self, newName):
        self.name = newName
    
    def changeAge(self, newAge):
        self.age = newAge
    
    def changePhone(self, newPhone):
        self.phone = newPhone
    

