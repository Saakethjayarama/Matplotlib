import matplotlib.pyplot as plt
import numpy as np

xlist = np.linspace(-3.0,3.0,100)
ylist = np.linspace(-3.0,3.0,100)

x, y = np.meshgrid(xlist, ylist)
z = np.sqrt(x**2+y**2)

fig, axes = plt.subplots(1,1)
cp = axes.contourf(x, y, z)
fig.colorbar(cp)

plt.show()