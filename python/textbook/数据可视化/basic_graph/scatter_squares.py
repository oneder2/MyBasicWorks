import matplotlib.pyplot as plt


upper_lim = 500
x_values = list(range(1, upper_lim + 1))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolors = "none", s = 40)

# 设置图标标题并给坐标轴加标签
plt.title("Square Number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置标记的大小
plt.tick_params(axis = "both", which = "major", labelsize = 14)

plt.axis([0, upper_lim*1.05, 0, ((upper_lim) ** 3) * 1.05])

plt.savefig("squares_plot.png", bbox_inches = "tight")

plt.show()
