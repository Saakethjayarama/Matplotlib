import numpy as np
import matplotlib.pyplot as plt

labels = ['C1', 'C2', 'C3']
men = [12, 20, 13]
women = [13, 19, 13]
width = 0.35
x = np.arange(len(labels))

figure = plt.figure()
ax = figure.add_axes([0,0,1,1])
ax.bar(x-width/2, men, width, label="Men"  )
ax.bar(x+width/2, women, width, label="Women")

ax.set_title('Votes')
ax.set_ylabel('Count')
ax.set_xlabel('Cities')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()