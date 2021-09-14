import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()
ax = figure.add_axes([0,0,1,1])

x = np.arange(3)
y = [
  [10,12,13],
  [7,6,3],
  [5,9,12]
]

width = 0.25

ax.bar(x, y[0], color='r', width=width)
ax.bar(x+0.25, y[1], color='g', width=width)
ax.bar(x+0.5, y[2], color='b', width=width)

plt.show()