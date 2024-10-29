import json


d = {'s':'you','d':'are'}   #给一个字典
j = json.dumps(d)
print(type(j))
print(j)

d1 = json.loads(j)
print(type(d1))
print(d1)
