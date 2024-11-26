output = []
for i in range(12):
    output.append(int(input()))

current = 0
save = 0
for i in range(12):
    cost = output[i]
    current += 300
    current -= cost
    while current >= 100:
        current -= 100
        save += 1
    if current < 0:
        print(-(i+1))
        break
if current >= 0:
    print(save * 120 + current)
    
        
