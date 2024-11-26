from calculator import *
# from solveVariety import *

# 输入参数
# exeInit = int(input("请输入整数精确位数："))
# stepInit = int(input("请输入初始步长："))
# y = int(input("请输入方程相等的值："))

inputFormula = Formula(3, (1,2,3,4), 1)
calculator = FormulaSolver(formula=inputFormula, test = 1, y = 0, exe = 6)
print(calculator.approching())

# f = Formula(3, (1,2,3,4), 1)
# print(f.resultOut(2))

