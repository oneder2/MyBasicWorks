with open("text.txt", "r") as f:
    context = f.read()

# 突然忘了怎么切片了
# print(context[::])

result = ""
for i in context:
    result = i + result
print(result)