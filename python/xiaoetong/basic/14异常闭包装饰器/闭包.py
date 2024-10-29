# 定义一个外部函数
def fun1():
    # 定义一个变量
    num1 = 1
    # 定义一个内部函数
    def fun2():
        # 对num1相加一个1
        num2 = num1 + 1
        print(num2)
    
    return fun2

def out1(a):
    # 定义一个内部函数
    def inner1(b):
        # 在内部函数使用外部函数的参数
        result = a + b
        print(f"结果为：{result} = {a} + {b}")
    return inner1

f = out1(3)
f(7)
f(4)