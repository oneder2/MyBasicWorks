def cut_and_spare(array, x : int, y : int, depth : int):
    length = len(array)
    if  length // 2**(depth-1) != 1:
      #  breakpoint()
        array = quarter_to_zero(array, x, y, depth)
        depth += 1
        cut_and_spare(array, x, y + length//2**(depth-1), depth)
        cut_and_spare(array, x + length//2**(depth-1), y, depth)
        cut_and_spare(array, x + length//2**(depth-1), y + length//2**(depth-1), depth)
    return 

def quarter_to_zero(array, x, y, depth):
    length = len(array)
    size = length//(2**depth)
    for i in range(y, y + size):
        for j in range(x, x + size):
            array[i][j] = 0
    return array


scale = 2**int(input())

test = [[1 for _ in range(scale)] for __ in range(scale)]
#test = quarter_to_zero(test, 0, 0, 3)
cut_and_spare(test, 0, 0, 1)

for row in test:
    print(" ".join(map(str, row)))

