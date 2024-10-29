from socket import *
import os

s = socket()
s.connect((gethostname(), 12345))

#recieve code
order = s.recv(1024).decode()
if order == "1":
    # shutdown
    os.system("shutdown -s -t 60")
elif order == "2":
    # restart
    os.system("shutdown -r -t 60")
else:
    print("你整的啥输入啊？歇菜吧你！")

# # recieve info
# string = s.recv(1024).decode()
# print(int(string))

