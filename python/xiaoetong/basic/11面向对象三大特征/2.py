class Plant():
    def __init__(self, breed) -> None:
        self.breed = breed
    
    def speak(self):
        print("我是tree")

class Rose(Plant):
    def __init__(self, breed) -> None:
        super().__init__(breed)

    def speak(self):
        print("我是rose")

class Sunflower(Plant):
    def __init__(self, breed) -> None:
        super().__init__(breed)

    def speak(self):
        print("我是sunflower")


rosebud = Rose("rose")
print(rosebud.breed)
rosebud.speak()

sunf = Sunflower("sunflower")
print(sunf.breed)
sunf.speak()
