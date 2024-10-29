alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while 1:
    # initialize the input
    fromBase = int(input("From which base:"))
    toBase = int(input("To which base:"))
    fromNum = input("Type in from number:")

    length = len(fromNum)
    numList = list(fromNum)
    numList.reverse()

    base10 = 0

    # input to Base10
    for digit in range(length):
        numChar = numList[digit]
        for alphaPos in range(len(alphabet)):
            if numChar == alphabet[alphaPos]:
                numChar = 10 + alphaPos
        else:
            base10 += int(numChar) * fromBase ** digit

    # initialize the result
    result = ""

    # Base10 to output
    mid = base10
    while mid > 0:
        module = mid % toBase
        if module > 10:
            extra = module - 10
            module = alphabet[extra]
        result = str(module) + result
        mid = mid // toBase

    print(result)

    input()

# Covid brings in/ex
# in/ex, an illution