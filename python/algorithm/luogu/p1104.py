# 输入人数
student_num = int(input())
students = []
for _ in range(student_num):
    # 输入学生信息
    input_list = input().split(" ")
    # 记录学生信息
    student = {}
    name = input_list[0]
    year = input_list[1]
    month = input_list[2]
    # 生日日期格式化
    if len(month) == 1:
        month = "0" + month
    day = input_list[3]
    if len(day) == 1:
        day = "0" + day
    # 字符串拼接后将日期整合为一个整形数字
    birth = int("".join([year, month, day]))

    # 将信息存储在一个字典中
    student["name"] = name
    student["birth"] = birth

    # 更新学生列表
    students.append(student)

# 将字典列表倒序，目的是为了在排序之后让相同生日但是后输入的人先输出
ans = students[::-1]

# 根据生日日期排序
ans = sorted(ans, key=lambda item:item["birth"])

# 输出一个字符串，用“\n”换行
print ("\n".join(student["name"] for student in ans))

# 此前也尝试过直接用for循环：
#for student in ans:
#  print(student["name"])
# 效果一致，但是仍然没有变化

