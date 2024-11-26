num = input()

ans = ""
if "." in num:
    numList = num.split(".")
    left = numList[0][::-1].lstrip("0")
    right = numList[1][::-1].rstrip("0")
    if left == "":
        left = "0"
    if right == "":
        right = "0"
    ans += left + "." + right

elif "/" in num:
    numList = num.split("/")
    left = numList[0][::-1].lstrip("0")
    right = numList[1][::-1].rstrip("0")
    if left == "":
        left = "0"
    if right == "":
        right = "0"
    ans += left + "/" + right

elif "%" in num:
    output = num[:-1][::-1].lstrip("0")
    if output == "":
        output = "0"
    ans += output + "%"

else:
    ans += num[::-1].lstrip("0")
    if ans == "":
        ans += "0"

print(ans)
