import requests


url = "https://i2.3conline.com/images/piclib/201111/20/batch/1/117693/1321788711736t222yhr6li.jpg"

res = requests.get(url)
# 如果获取到的是媒体数据，输入文件是二进制文件
# print(res.text) # 该段代码会生成一段由于解码形式有误而产生的一段字符串
# print(res.content) # 该段代码会获取一个二进制字节数据字符，格式诸如：b'\...\...'

# 将获取的数据写入到文件中
with open("蕾米莉亚&芙兰朵露.png", "wb") as f:
    # 向文件中写入内容
    f.write(res.content)

