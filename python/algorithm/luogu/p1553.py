def beforeString(string, target):
    output = ""
    for c in string:
        if c != target:
            output += c
        else:
            return output

def afterString(string, target):
    output = ""
    for i in range(len(string) - 1, -1, -1):
        if string[i] != target:
            output = string[i] + output
        else:
            return output

def reverseNum(num):
    return str(int(str(num)[::-1]))


realnum = input()

if realnum == "":
    print()
elif "." in realnum:
    print(
            str(
                float(
                    reverseNum (beforeString (realnum, ".")) + "." + reverseNum (afterString (realnum, "."))
                    )
                )
            )
elif "/" in realnum:
    print(
            reverseNum (beforeString (realnum, "/")) + "/" + reverseNum (afterString (realnum, "/"))
            )
elif "%" in realnum:
    print(
            reverseNum (beforeString (realnum, "%")) + "%"
            )
else:
    print(
            reverseNum (realnum)
            )

    
