class Car():
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
    
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getYear(self):
        return self.year
    

A = Car("十里河", "大众", "2024")
print(A.getMake())
print(A.getModel())
print(A.getYear())
