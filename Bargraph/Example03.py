import numpy as np
import matplotlib.pyplot as plt

x = ["C1", "C2", "C3"]
men_count = [10,20,30]
women_count = [5,10,15]

figure = plt.figure()
ax = figure.add_axes([0,0,1,1])
ax.bar(x, men_count, label="Men", width=0.25)
ax.bar(x, women_count, label="Women", width=0.25, bottom=men_count)

ax.set_ylabel("Head count")
ax.set_xlabel("Cities")
ax.set_title("Votes in cities")
ax.legend()


plt.show()