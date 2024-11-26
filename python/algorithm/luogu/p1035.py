k = int(input())

added = 0
n = 1
while added <= k:
    added += 1/n
    if added <= k:
        n+=1
print(n)
