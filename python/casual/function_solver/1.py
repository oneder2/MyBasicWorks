# 总成绩=作业成绩×20%+小测成绩×30%+期末考试成绩×50%

raw_input = input()
listInput = raw_input.split()

h = int(listInput[0])
q = int(listInput[1])
e = int(listInput[2])

print(h * 0.2 + q * 0.3 + e * 0.5)