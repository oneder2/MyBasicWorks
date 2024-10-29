height = int(input("请输入身高："))
weight = int(input("请输入体重："))

BMIvalue = weight/(height**2)

if BMIvalue < 18.5:
    print("较轻")
elif 18.5 < BMIvalue < 24.9:
    print("正常")
elif 24.9 < BMIvalue < 29.9:
    print("超重")
elif 29.9 < BMIvalue:
    print("肥胖")
else:
    print("Bad input")



