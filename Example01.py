import matplotlib.pyplot as plt

figure = plt.figure()
ax = figure.add_axes([0,0,1,1], "Subject", "Students")

lang = ['C', 'C++', 'Py', 'js']
students = [5,10,3,7]
ax.bar(lang, students)

plt.show()