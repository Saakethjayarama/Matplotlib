# Grids

import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1,3)
x = np.arange(1, 11)

axes[0].plot(x, x**3, 'g', lw=1)
axes[0].grid(True)
axes[0].set_title('Default Grid')

axes[1].plot(np.arange(-1, 3), np.arange(3, 7), color="r")
axes[1].grid(color='r', lw=1, ls='-.')
axes[1].set_title('Custom grid')

axes[2].scatter(np.arange(-1, 3), np.arange(3, 7), color="r")
axes[2].set_title('No grid')

plt.show()