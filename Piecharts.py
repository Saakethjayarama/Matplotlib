# Piechart example

import matplotlib.pyplot as plt


fig =plt.figure()
axes= fig.add_axes([0,0,1,1])
categories = ['java', 'python', 'c', 'js']
usage = [80, 10, 10, 10]
axes.pie(usage, labels=categories, autopct='%1.2f%%')
plt.show()