class student():
    def __init__(self, index, acadamicScore, exploringScore):
        self.index = index
        self.acadamicScore = acadamicScore
        self.exploringScore = exploringScore
        self.generalScore = (self.acadamicScore * 7) + (self.exploringScore * 3)
    
    def ifQualified(self):
        return self.acadamicScore + self.exploringScore > 140 and self.generalScore >= 800


length = int(input())
students = []
for i in range(length):
    rawList = input().split(" ")
    students.append(
        student(
            int(rawList[0]), 
            int(rawList[1]), 
            int(rawList[2])
            )
        )

for student in students:
    if student.ifQualified():
        print("Excellent")
    else:
        print("Not excellent")
