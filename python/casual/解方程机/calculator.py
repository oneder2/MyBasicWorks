import time
import numpy
from functionBase import *
from solveVariety import Formula

# 计算器类
# 初始化接受：
# 1. 公式是什么
# 1. 初始测试值
# 3. 初始步长
# 4. 与多项式相等的值
# 5. 精度（小数点后几位）
# 
# 功能：
# 1. 保存一个等式的所有元素
# 2. change类函数，改变初始化出事的所有参数
# 3. approach函数，构造等式之后可以进行拟合求解，并返回数值解
# 4. 

# y = 1
# test = 0
# exe = 3
# step = 10

# 

class FormulaSolver():
    def __init__(self, 
                 formula:Formula,
                 test: float = 0, 
                 y: float = 1, 
                 step: float = 10, 
                 exe: int = 3, 
                 ) -> None:
        self.formula = formula
        self.test = test
        self.y = y
        self.step = step
        self.exe = exe

    def changeFormula(self, newFormula):
        self.formula = newFormula

    def changeTest(self, newTest):
        self.test = newTest

    def changeY(self, newY):
        self.y = newY

    def changeStep(self, newStep):
        self.step = newStep

    def changeExe(self, newExe):
        self.exe = newExe
    
    def approching(self):
        # 循环拟合条件：误差大于精确位
        while abs(self.formula.calculate(self.test)) >= 10**(-self.exe):
            
            # Debug用
            print(self.test)
            time.sleep(0.5)

            # 如果相等，直接输出
            if self.formula.returnPrint() == self.y:
                break

            # 如果计算值偏大，以步长为尺度，减小测试值
            while self.formula.calculate(self.test) > self.y:
                print(self.formula.returnPrint(), self.y)
                print(self.step)
                self.test -= self.step

            # 如果计算值偏小，以步长为尺度，增大测试值，并进行至当前精确度的极限值
            while self.formula.calculate(self.test) < self.y:
                self.test += self.step

            # 进一步降低步长
            if 10**(self.exe) > self.step: # 如果步长小于精确度，降低步长
                self.step *= 0.1
                
            else: # 如果步长大于精确度，证明此时已经到达最小步长，可以直接输出
                break

        return self.test
