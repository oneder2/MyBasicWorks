from functionBase import *

e = 2.71828

# 类：多项式
# 用于储存并操作一个多项式

# 初始化接受：
# 1. 最高次
# 2. 各项系数（元组）
# 3. x初始值（用于计算）
# 将初始化计算值储存在局部变量中备用
# 
# 功能：
# 可以返回且仅返回计算值结果
# 可以更新参数再次进行计算，更新并返回计算结果

class Formula():    
    # 初始化，输入最高次，各项系数，以及x值
    def __init__(self, maxOrder, factors, x):
        self.maxOrder = maxOrder
        self.factors = factors
        self.outPut = self.calculate(x)
        self.result = 0
    
    # 计算
    def calculate(self, x):
        result = 0
        for index, content in enumerate(self.factors):
            if index == 0:
                result += content
            else:
                result += content * x **self.factors[index]
        self.outPut = result
        return self.outPut

    # 不计算，只返回结果
    def returnPrint(self):
        return self.outPut


# # 测试函数
def function(x):
    return (x - e**(-x**2))