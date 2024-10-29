def reverse_edge(Input):
    for i in range(len(Input) // 2):
        Input[i], Input[len(Input) - i] = Input[len(Input) - i], Input[i]
    return Input

def reverse_swap(Input):
    for i in range(len(Input)):
        Pop = List.pop()
        Input.insert(i, Pop)
    return Input


List = [1,2,3,4,5]



List = reverse_swap(List)

print(List)