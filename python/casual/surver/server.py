from socket import *

S = socket()

S.bind((gethostname(), 8888))

S.listen()

s, addr = S.accept()

print(addr)

