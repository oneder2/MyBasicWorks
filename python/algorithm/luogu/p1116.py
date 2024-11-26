length = int(input())
num_list = input().split(" ")
while len(num_list) != length and length != 0:
    num_list += input().split(" ")
num_list = list(map(int, num_list))

count = 0
for _ in range(length):
    for i in range(0, length-1):
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            count += 1

print(count)



