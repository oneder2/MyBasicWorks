def stack_output(operate_array: list[int], 
                 mid_stack: list[int], 
                 output: list[int], 
                 opcode : int, 
                 count : set):
    # if mid_stack and operate_array is empty, there is a output, return
    if len(mid_stack) == 0 and len(operate_array) == 0:
        count.add(tuple(output))
        return
    # opcode == 1, pop from operate_array to mid_stack
    if opcode == 1 or opcode == 0:
        if len(operate_array) == 0:
            stack_output(operate_array, mid_stack, output, -1, count)
        mid_stack.append(operate_array.pop())
    # opcode == -1, pop from mid_stack to output
    elif opcode == -1:
        if len(mid_stack) == 0:
            stack_output(operate_array, mid_stack, output, 1, count)
        output.append(mid_stack.pop())
    breakpoint()


max_num = int(input())
operator = [i for i in range(max_num, 0, -1)]
stackA = []
output = []
count = set()
stack_output(operator, stackA, output, 0, count)
print(count)

