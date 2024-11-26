# i input a num string, return True if is a prime number, return False if not
def IsPrime(intnum):
    strnum = str(intnum)
    # all about 5
    if int(strnum[-1]) == 5 or int(strnum[-1]) % 2 == 0:
        return False
    # general way
    num = int(strnum)
    for i in range(3, int(num**0.5) + 1, 2): 
        if num % i == 0:
            return False
    return True


inputNum = int(input())
# if input is prime num
if IsPrime(inputNum):
    print(inputNum)
elif inputNum % 2 == 0:
    print(inputNum // 2)
elif inputNum % 3 == 0:
    print(inputNum // 3)
elif inputNum % 5 == 0:
    print(inputNum // 5)
else:
    for i in range(7, int(inputNum ** 0.5) + 1, 2):
        if IsPrime(i) and inputNum % i == 0:
            print(inputNum // i)
            break

