# def isPrime(num):
#     if num == 1:
#         return False
# 
#     for i in range(3, num//2 + 1, 2):
#         if num % i == 0:
#             return False
#     return True
# 
# 
# 
# maxMess = 2
# currentMess = 0
# amount = 0
# 
# if maxMess >= 2:
#     currentMess = 2
#     amount = 1
#     print(2)
#     i = 3
#     while 1:
#         if isPrime(i):
#             if currentMess + i <= maxMess:
#                 currentMess += i
#                 amount += 1
#                 print(i)
#             else:
#                 break
#         i += 2
# 
# print("______________")
# print(currentMess)
# print(amount)

def isPrime(num):
    if num == 1:
        return False

    for i in range(3, num//2 + 1, 2):
        if num % i == 0:
            return False
    return True



maxMess = 2
currentMess = 0
amount = 0

if maxMess >= 2:
    currentMess = 2
    amount = 1
    print(2)
    i = 3
    while 1:
        if isPrime(i):
            if currentMess + i <= maxMess:
                currentMess += i
                amount += 1
                print(i)
            else:
                break
        i += 2

print(amount)
