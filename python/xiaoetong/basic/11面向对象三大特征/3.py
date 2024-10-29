class Fruit():
    def makejuice(self):
        print("我能榨汁")

class Apple(Fruit):
    def makejuice(self):
        print("我能榨苹果汁")

class Banana(Fruit):
    def makejuice(self):
        print("我能榨香蕉汁")

class Orange(Fruit):
    def makejuice(self):
        print("我能榨橘子汁")

def Squeeze(fruit):
    # 接口（近似理解成：定义一种方法，并对于传入的对象调用这一种方法）
    fruit.makejuice()

an_orange = Orange()
Squeeze(an_orange)

