# 如果三条线段不能组成一个三角形，输出Not triangle；
def isTriangle(i, j, l):
    if i + j > l:
        return True
    return False;

# 如果是直角三角形，输出Right triangle；
def isRight(i, j, l):
    if i**2 + j**2 == l**2:
        return True
    return False

# 如果是锐角三角形，输出Acute triangle；
def isAcute(i, j, l):
    if i**2 + j**2 > l**2:
        return True
    return False

# 如果是钝角三角形，输出Obtuse triangle；
def isObtuse(i, j, l):
    if i**2 + j**2 < l**2:
        return True
    return False

# 如果是等腰三角形，输出Isosceles triangle；
def isIsosceles(i, j, l):
    if i == j:
        return True
    return False

# 如果是等边三角形，输出Equilateral triangle。
def isEquilateral(i, j, l):
    if i == j and j == l:
        return True
    return False


rawInputList = input().split(" ")
intInputList = [int(i) for i in rawInputList]
intInputList.sort()
a = int(intInputList[0])
b = int(intInputList[1])
c = int(intInputList[2])

ans = ""
# 是不是三角形：
if isTriangle(a, b, c):
    if isRight(a, b, c):
        ans += "Right triangle" + "\n"
    if isAcute(a, b, c):
        ans += "Acute triangle" + "\n"
    if isObtuse(a, b, c):
        ans += "Obtuse triangle" + "\n"
    if isIsosceles(a, b, c):
        ans += "Isosceles triangle" + "\n"
    if isEquilateral(a, b, c):
        ans += "Equilateral triangle" + "\n"
        
else:
    ans += "Not triangle"

ans = ans.rstrip("\n")

print(ans)
