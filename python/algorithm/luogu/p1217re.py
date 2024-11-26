# i input a num string, return True if is a prime number, return False if not
def IsPrime(strnum):
    # all about 5
    if int(strnum[-1]) == 5:
        return False
    # general way
    num = int(strnum)
    for i in range(3, int(num**0.5) + 1, 2): 
        if num % i == 0:
            return False
    return True

# input a num string, return True if it is a palindrome value return False if it is not
def IsPalindrome(string):
    return string == string[::-1]

# find the upper six's times number, as prime number is always near the 6x
def FindUpperSix(num):
    modsix = num % 6
    if modsix == 0:
        return num
    return num + (6 - modsix)
# goto part without: (first number is even) or (length is even)
def BitGoto(num):
    str_num = str(num)
    length = len(str_num)
    # if the first bit is even, add the (length-1) * 10
    if length > 2 and (int(str_num[0]) % 2 == 0 or int(str_num[0]) == 5):
        print("______")
        return FindUpperSix(num + 10 ** (length - 1) - 6)
    # if the length is even, goto a higher bit
    if length % 2 == 0 and length != 2:
        print("____________")
        return FindUpperSix((10 ** length) - 6)
    return num


# input the data
rawInput = input().split(" ")
l = int(rawInput[0])
r = int(rawInput[1])

# boundary check
if IsPrime(str(l)) or l == 5:
    print(l)

x = FindUpperSix(l)
while x < r and x < 10000000:
    for i in range(-1, 3, 2):
        strnum = str(x+i)
        if IsPalindrome(strnum) and IsPrime(int(strnum)):
            print(strnum)
    x = BitGoto(strnum) # if broken, comment this line
    x += 6
