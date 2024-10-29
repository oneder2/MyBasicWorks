def Overadding(A, B):
    #将A和B编组
    pair = (A, B)
    #设定一个数组（a, b），True意味着a = a + b, False意味着b = a + b
    Mid = True
    #储存历史记录，防止循环
    History = []

    while A + B != 10:#辗转相加
        if Mid == True:
            A = OverAdd(A, B)
            Mid = False
        else:
            B = OverAdd(B, A)
            Mid = True
        Group = ( A, B )
        if Group in History:#判断循环
            print ( pair, " 为起始", len ( History ) , "次后，陷入循环" )#写出循环所需最少次数，并终止
            break
        else:
            History.append(Group)
    else:
        print ( pair, " 为起始", len ( History ) ,  "次后有解" )#写出满足 a + b = 10 所需循环次数

    print(History)#输出历史数据

    return()

#定义一个函数返回m = m + n
def OverAdd (m, n):
    Index = str(m + n)
    Return = int(Index[len(Index) - 1])
    return Return

while True:
    Input = input("请输入回车开始展示：")
    if Input == "":
        break
    else:
        print("同志，输入回车，“Enter”")

a = int ( input ( "先合数：" ) )
b = int ( input ( "后合数：" ) )

Overadding(a, b)

input()#等

