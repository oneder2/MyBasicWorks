import re


numberInput = input("请输入一个手机号：")

if len(numberInput) == 11:
    print("该手机号合法")
else:
    print("请输入正确手机号")
    exit()

# 如果只取前三位，时间开销会不会低一些
pre3 = numberInput[:3]

mobile = re.match(r"13[456789]|14[78]|15[012789]|165|178|18[23478]", pre3)
if mobile != None:
    print("运营商是中国移动")

unicon = re.match(r"13[012]|14[056]|15[56]|166|17[56]|18[56]", pre3)
if unicon != None:
    print("运营商是中国联通")

telecon = re.match(r"133|149|153|17[37]|18[019]|19[19]", pre3)
if telecon != None:
    print("运营商是中国电信")
