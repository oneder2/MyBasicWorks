def stepMult(num):
    output = 1
    for i in range(1, num + 1):
        output *= i
    return output

rawinput = int(input())

ans = 0
for i in range(1, rawinput + 1):
    ans += stepMult(i)

print(ans)
