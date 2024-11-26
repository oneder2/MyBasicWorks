#!/usr/bin/python
import math

def is_prime(n):
    if n<2:
        return False
    for i in range(2,1+int(math.sqrt(n))):
        if n%i==0:
            return False
    return True


def within_bound(num, lbound, rbound):
    return (num >= lbound and num <= rbound)

raw_input_list = input().split(" ")
l = int(raw_input_list[0])
r = int(raw_input_list[1])

output = []
for a in range(0,9999):
    s = str(a)
    rev=s+s[::-1]
    if is_prime(int(rev)) and within_bound(int(rev), l, r):
        output.append(rev)
#        print(rev)
    rev=s+s[::-1][1::]
    if is_prime(int(rev)) and within_bound(int(rev), l, r):
        output.append(rev)
#        print(rev)

output = list(map(int, output))
output.sort()
for i in output:
    print(i)
