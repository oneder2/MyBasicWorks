import json


with open("身份证码值对照表.json",  "r", encoding="utf-8") as file:
    idSheet = json.load(file)

print(idSheet)

idInput = input("请输入前六位身份证号：")
print("所在区域为：" + idSheet[idInput])

