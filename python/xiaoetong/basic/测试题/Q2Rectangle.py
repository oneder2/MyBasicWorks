class Rectangle():
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def getCiruit(self):
        circuit = 2 * (self.width + self.length)
        return circuit
    
    def getArea(self):
        area = self.width * self.length
        return area
    
r1 = Rectangle(20, 10)
print(f"长方形的周长是：{r1.getCiruit()}")
print(f"长方形的面积是：{r1.getArea()}")