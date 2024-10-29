from random import shuffle
from time import localtime
from sys import exit


# 创造同学成员列表
Student = [] # 读取“全体同学”，生成列表
filename = "全体同学.txt" 
with open(filename, encoding='utf-8') as file_object:
    print(file_object)
    for line in file_object:
        Student.append(line.rstrip())

for check in Student: # 检测“全体同学.txt”中有无数字
    try:
        check = int(check)
    except ValueError:
        continue
    else:
        with open("Arranging.txt", "a") as file_object:
            file_object.write("\n————！！异常！！————“全体同学.txt”文件中似乎混入了奇怪的东西，但本程序仍将运转\n")

# 使格式一致
maxlen = 0
for student in Student: # 检测最大名字字数
    if maxlen < len(student):
        maxlen = len(student)

for reg in range(len(Student)):
    diff = maxlen - len(Student[reg])
    for i in range(diff):
        Student[reg] = Student[reg] + " _ "

# 创造一个“1”——“学生数”的数列后打乱
Num = len(Student)
List = []
for i in range (Num):
    index = i + 1
    List.append(index)
shuffle(List)


# 创造一个指定列数，自适应行数的二位数组
with open("座位列数.txt") as file_object: # 读取最大列数
    try:
        column = int(file_object.readlines()[0])
    except ValueError:
        with open("Arranging.txt", "a") as file_object:
            file_object.write("\n————！！异常！！————请检查文件“座位列数.txt”第一行是否为正整数")
        exit()

row = 1

while row * column < Num:
    row += 1

arrange = []

for y in range(row):
    arrange.append([])
    for x in range(column):
        arrange[y].append(0)


# 添加空位
loss = row * column - Num

warn = False # 检测最后一排人数是否过少
if column // (3/2) > loss:
    warn = True

sidemark = True # True为左边，False为右边
index, differ = 0, 0

# 根据最长名字制造空格
void = ""
for i in range(maxlen):
    void = void + " _ "

while loss > 0: # 进行填空
    if sidemark:
        arrange[len(arrange) - 1][index + differ] = void
    else:
        arrange[len(arrange) - 1][column - 1 - differ] = void

    loss -= 1 # 更新参数
    if not sidemark:
        differ += 1
    sidemark = not sidemark


# 依次赋值
ind = 0
for y in range(row):
    for x in range(column):
        if arrange[y][x] == void:
            continue
        arrange[y][x] = Student[List[ind-2] - 1]
        ind += 1


#设计输出格式
output = []
for row in arrange:
    line = ""
    for colunm in row:
        line  = line + "{" + colunm + "}"
    output.append(line)


#生成日期
timestamp = ""
year, month, day = localtime()[0], localtime()[1], localtime()[2]
timestamp = str(year) + "年" + str(month) + "月" + str(day) + "日"


#存储信息
with open(timestamp + "排座位.txt", "a") as file_object:
    file_object.write(timestamp + "\n")
    file_object.write("窗————————讲台————————门\n")
    for i in output:
        file_object.write(i + "\n")
    if warn:
        file_object.write("最后一排人略少，本排列结果仅供参考\n")
