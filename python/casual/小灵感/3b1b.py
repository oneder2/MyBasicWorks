def phi(num):
    return (1 + 1 / num)

x = -0.618

for i in range(100):
    print(x, i)
    x = phi(x)
