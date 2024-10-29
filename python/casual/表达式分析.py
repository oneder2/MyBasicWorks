present = input("请输入待计算表达式：")

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

calcu = ["+", "-", "*", "/"]


def pre_calculate(char, length, num_stack):
    if char == "+":
        num_stack.append( num_stack.pop( length - 1 ) + num_stack.pop( length - 2 ) )
    elif char == "-":
        num_stack.append( num_stack.pop( length - 1 ) - num_stack.pop( length - 2 ) )
    elif char == "*":
        num_stack.append( num_stack.pop( length - 1 ) * num_stack.pop( length - 2 ) )
    elif char == "/":
        num_stack.append( num_stack.pop( length - 1 ) / num_stack.pop( length - 2 ) )
    return num_stack

def pre_analize(present, num_stack):
    for char in present:
        if char in num:
            num_stack.append(int(char))
        elif char in calcu:
            length = len(num_stack)
            num_stack = pre_calculate(char, length, num_stack)

def mid_analize(present, num_stack):
    for char in present:
        pass


num_stack = []

pre_analize(present, num_stack)

print(num_stack)