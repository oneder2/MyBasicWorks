# a.py 
var1 = 1

def changeVar1():
    global var1
    var1 = 2
    print(f'in a: var1 is {var1}')