# return if it is prime number
def IsPrime(num):
    if num < 2: # negative, 0, 1 exclude
        return False
    if num  == 2: # include 2
        return True
    for i in range(3, int(num**0.5) + 1, 2): # general method
        if num % i == 0:
            return False
    return True

# input word string
word = input()
# hashmap, statistic how much times each letters appear
hashmap = {}
for i in word:
    if not i in hashmap:
        hashmap[i] = 1
    else:
        hashmap[i] += 1

maxKey, maxValue = 0, 0
minKey, minValue = 0, 101
for key, value in hashmap.items():
    if value < minValue:
        minKey, minValue = key, value
    if value > maxValue:
        maxkey, maxValue = key, value

differ = maxValue - minValue
if IsPrime(differ):
    print("Lucky Word")
    print(differ)
else:
    print("No Answer")
    print(0)
