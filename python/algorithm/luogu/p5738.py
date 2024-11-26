param_input = input().split(" ")
stu_num = int(param_input[0])
rec_num = int(param_input[1])

final_score_list = []

if rec_num <= 2:
    for _ in range(stu_num):
        input()
    print("0.00")
else:
    for _ in range(stu_num):
        score_list = input().split(" ")
        for i in range(rec_num):
            score_list[i] = int(score_list[i])
        score_list.sort()
        score_list.pop()
        score_list.pop(0)
        final_score_list.append(sum(score_list)/(rec_num-2))
    ans = round(max(final_score_list), 2)
    if ans % 1 == 0:
        ans = str(ans) + "0"
    print(ans)
