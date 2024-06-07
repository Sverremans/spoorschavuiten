import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import spoorschavuiten.code.main_script as ms
plt.style.use('_mpl-gallery')

# # make the data
sizes = 10 # np.random.uniform(15, 80)
colors = "black"

for station in ms.holland._stations:
    x = station._x
    y = station._y

    fig, ax = plt.subplots()

    ax.scatter(x, y, s=sizes, c=colors)
# np.random.seed(3)
# x = 1
# y = 4
# size and color:
 # np.random.uniform(15, 80)
# plot


ax.set(xlim=(0, 60), xticks=np.arange(0, 60),
       ylim=(0, 60), yticks=np.arange(0, 60))

# plt.savefig('scatterplot.png')

plt.show()