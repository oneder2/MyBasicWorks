from socket import *

s = socket()

s.connect((gethostname(), 8888))