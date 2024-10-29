students = [
{'name' : '张三', 'age' : 23, 'score' : 88, 'tel' : '23423532', 'gender' : '男'},
{'name' : '李四', 'age' : 26, 'score' : 80, 'tel' : '12533453', 'gender' : '女'},
{'name' : '王五', 'age' : 15, 'score' : 58, 'tel' : '56453453', 'gender' : '男'},
{'name' : '赵六', 'age' : 16, 'score' : 57, 'tel' : '86786785', 'gender' : '不明'},
{'name' : '小明', 'age' : 18, 'score' : 98, 'tel' : '23434656', 'gender' : '女'},
{'name' : '小红', 'age' : 23, 'score' : 72, 'tel' : '67867868', 'gender' : '女'}
]

disQulified = []
for student in students:
    if student["score"] < 60:
        disQulified.append(student["name"])

print(f"一共有{len(disQulified)}人不及格")
print(f"他们是：{disQulified}")