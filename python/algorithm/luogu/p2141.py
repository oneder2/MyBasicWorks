# how many numbers in all
length = int(input())
qnums = input().split(" ")
# make input string into int
for i in range(0, length):
    qnums[i] = int(qnums[i])
qnums.sort()

# "how many" no repeating
ans = set()
for x in range(0, length):
    for y in range(x, length):
        if x == y:
            continue
        for z in range(0, length):
            if x == z or y == z:
                continue
            if qnums[x] + qnums[y] == qnums[z]:
                ans.add(qnums[z])
print(len(ans))
