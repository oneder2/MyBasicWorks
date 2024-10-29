import matplotlib.pyplot as plt

array = []
squares = []

for i in range(1, 6):
    array.append(i)
    squares.append(i**2)

plt.plot(array, squares, linewidth = 5)

# 设计图表主题，并给坐标加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记大小
plt.tick_params(axis = "both", labelsize = 14)

plt.show()
