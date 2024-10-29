import csv
from datatime import datatime

from matplotlib import pyplot as plt

# 从文件中获取日期和最高气温
filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datatime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

# 根据数据绘制图形
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = "red")

# 设置图形格式
plt.title("Daily high tempretures - 2014", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Tempreture(F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
