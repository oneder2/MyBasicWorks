def up_stair(N, deepth = 0):
    global count
    global steps

    if N == 0:
        print(steps)
        count += 1
        return
    
    if N < 0:
        return
    
    for i in range(1,4):
        steps.append(i)
        up_stair(N-i, deepth)
        steps.pop()


count = 0
steps = []

stairs = 5
up_stair(stairs)
print(count)