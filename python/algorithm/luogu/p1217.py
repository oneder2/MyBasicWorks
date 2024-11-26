# input a num string
# return True if it is a prime number
# return False if it is not
# input value should in [5, 100000000]

# specific restriction: this number should be a palindrome number first
def IsPrime(strnum):
    # all about 2 and 5
    if int(strnum[-1]) % 2 == 0 or int(strnum[-1]) == 5:
        return False
    
    # general way
    num = int(strnum)
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# input a num string,
# return True if it is a palindrome value
# return False if it is not
def IsPalindrome(string):
    if string == string[::-1]:
        return True
    return False

def BitGoto(string):
    length = len(string)
    intString = int(string)
    # if the first bit is even, add the (length-1) * 10 
    if length > 1:
        if int(string[0]) % 2 == 0 or int(string[0]) == 5:
            return intString + 10 ** (length-1)
    # if the length is even, goto a higher bit
    if length % 2 == 0:
        return 10 ** length - 1
    return intString


rawInput = input().split(" ")
l = int(rawInput[0])
r = int(rawInput[1])

if IsPrime(str(l)):
    print(l)
if l % 2 != 0:
    x = l
else:
    x = l + 1

# main cycle
while x < r:
    stringNum = str(x)
    if IsPalindrome(stringNum):
        x = BitGoto(stringNum)
        if IsPrime(stringNum):
           print(stringNum)
    if int(stringNum[0]) % 2 == 0:
        x =  x + 10 ** (len(stringNum)-1)
    x += 2





