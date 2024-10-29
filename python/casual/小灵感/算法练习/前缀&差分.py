def addup(listin):
    output = 0
    for i in listin:
        output = output + i
    return output


n = int(input(""))
List = input("")
numlist = List.split()
for i in range(n):
    numlist[i] = int(numlist[i])

print(numlist)

output = []

for i in range(n):
    output.append(addup(numlist[0:i+1]))

print(output)