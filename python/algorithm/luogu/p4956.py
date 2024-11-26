def amount(x, k):
    return x*7 + k*21

target = int(input()) // 52

x = 1
k = 1
while amount(x, k) != target:
    if k > 100:
        break
    if amount(x, k) > target or x >= 100:
        breakpoint()
        x = 1
        k += 1
    x += 1
else:
    print(x)
    print(k)
