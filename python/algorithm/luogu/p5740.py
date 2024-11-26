student_amount = int(input())
max_sum = -1
ans = ""
for _ in range(student_amount):
    raw_input = input()
    raw_input_list = raw_input.split(" ")
    added = int(raw_input_list[1]) + int(raw_input_list[2]) + int(raw_input_list[3])
    if max_sum < added:
        max_sum = added
        ans = raw_input
print(ans)
