# 3
# fafa 90 90 90
# lxl 95 85 90
# senpai 100 80 91
class Student():
    def __init__(self, name: str, score1: int, score2:int, score3: int):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.sumup = score1 + score2 + score3

    def __str__(self):
        return f"{self.name},{self.score1},{self.score2},{self.score3}"
    
    def get_sumup(self):
        print(self.sumup)
        

#students_infos = []
#for student in range(student_amount):
#    raw_list = input().split()
#    students_infos.append(Student(raw_list[0], int(raw_list[1]), int(raw_list[2]), int(raw_list[3])))



# amount of input students
student_amount =  int(input())
students = []
# students are stored like:
# [
#   {"name": xxx, "score1": 100, "score2": 100, "score3": 100},
#   {...},
#   .
#   {...}
# ]
for student in range(student_amount):
    raw_list = input().split()
    student = {
            "name" : raw_list[0],
            "score1" : int(raw_list[1]),
            "score2" : int(raw_list[2]),
            "score3" : int(raw_list[3]),
            "score_sum" : int(raw_list[1]) + int(raw_list[2]) + int(raw_list[3])
            }
    students.append(student)

ans = []
# sorting the student, according to score_sum'
students = sorted(students, key = lambda student: student["score_sum"])
# 
for i in range(student_amount):
    for j in range(i, student_amount):
        if i == j:
            continue
        if students[j]["score_sum"] - students[i]["score_sum"] <= 10 and abs(students[j]["score1"] - students[i]["score1"]) <= 5 and abs(students[j]["score2"] - students[i]["score2"]) <= 5 and abs(students[j]["score3"] - students[i]["score3"]) <= 5:
            if students[i]["name"] < students[j]["name"]:
                ans.append(" ".join([students[i]["name"], students[j]["name"]]))
            else:
                ans.append(" ".join([students[j]["name"], students[i]["name"]]))
# ensure the output follow alphabet
ans.sort()
for i in ans:
    print(i)

 #   while students[i]["score_sum"] - students[j]["score_num"]








