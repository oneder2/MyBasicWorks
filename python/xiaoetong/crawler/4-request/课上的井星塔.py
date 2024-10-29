height = 30


for i in range(height, -1, -1):
    print(" " * (i//4), end="\'")
    if i % 4 == 1:
        print("*" * (height - i))
    elif i % 4 == 3:
        print("#" * (height - i))
    