import json

data = {"a" : [1], "b" : 2}

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    re = json.load(f)
