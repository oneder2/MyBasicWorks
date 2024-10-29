from die import Die
import pygal

# 创建一个D6
die_1 = Die()
die_2 = Die()

print(die_1.roll())

# 投掷几次骰子，并将结果存储一个列表中
results = [die_1.roll() * die_2.roll() for roll_num in range(50000)]

# 分析结果
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 50000 times"


# 自动生成标签
hist.x_lables = (str(i) for i in range(1, max_result + 1))

# 设置表头
hist.x_title = "Result"
hist.y_title = "Frequency of result"

# 输出文件
hist.add('D6 * D6', frequencies)
hist.render_to_file('die_visual.svg')

# print(frequencies)
