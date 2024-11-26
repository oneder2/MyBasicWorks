inputSet = input().split(" ")

added = 0
for i in inputSet:
    added += int(i)

print(added * 2**(len(inputSet) - 1))
