from socket import *

# 1. wait for response
S = socket() # announce a socket
S.bind((gethostname(), 12345)) # bind socket
S.listen() # socket begin to listen
s, addr = S.accept()

# 2. send options out
print(addr)
print("distant tool")
print("1.shut down")
print("2.restart")
choise = input("请选择：")
s.send(choise.encode())

# # send info
# s.send(str(520).encode())
# # recieve info
# # s.recv()