plt.style.use("fivethirtyeight")
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_index = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_index - width, dev_y, label = "All Dev", width = width, color = "orange", linestyle = "-", linewidth = "3")

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640 ]

plt.bar(x_index, py_dev_y, label = "Python Dev",width = width, color = "black")

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_index + width, js_dev_y, label = "JavaScript Dev", width = width, color = "blue")

plt.xticks(ticks = x_index, labels = ages_x)
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.legend()
plt.tight_layout()
plt.title("Median Salary (USD) by Age", color = "k")
plt.show