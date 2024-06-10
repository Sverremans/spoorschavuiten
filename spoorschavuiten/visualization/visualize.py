import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import spoorschavuiten.code.main_script as ms
plt.style.use('_mpl-gallery')

# # make the data
sizes = 10
colors = "black"

print(ms.holland._stations)
x = []
y = []

for station in ms.holland._stations:
    x.append(station._x)
    y.append(station._y)

fig, ax = plt.subplots()
ax.scatter(x, y, s=sizes, c=colors)


ax.set(xlim=(4.2, 5.2), xticks=np.arange(4, 6),
       ylim=(51, 53), yticks=np.arange(50, 55))

# plt.savefig('scatterplot.png')
print(ms.holland._connections)

# plt.show()
# print(x)
# print(y)