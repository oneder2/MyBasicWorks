def fact(num):
    output = 1
    for i in range(1, num+1):
        output *= i
    return output


group_amount = int(input())
output_list = []
for _ in range(group_amount):
    raw_input_list = input().split(" ")
    fact_num = int(raw_input_list[0])
    target = raw_input_list[1]

    factorial = str(fact(fact_num))
    
    count = factorial.count(target)
    output_list.append(str(count))

print("\n".join(output_list))

