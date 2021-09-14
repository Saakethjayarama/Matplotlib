# Plot

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5)

plt.plot(x, x**x)
plt.title("X ^ X")
plt.xlabel("X")
plt.show()