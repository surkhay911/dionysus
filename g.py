from __future__ import print_function   # if you are using Python 2
import dionysus as d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#points2 = np.random.random((100, 2))
#print(points2)
#np.savetxt('example_1.txt',points2)

points1 = np.loadtxt('example_1.txt')
print(points1)
print(type(points1))


fig, ax = plt.subplots()


x1 = []
y1 = []
for i in range(len(points1)):
    x1.append(points1[i][0])
    y1.append(points1[i][1])
print(x1,y1)

points = [[j,k] for j,k in zip(x1,y1)]
print(x1, y1)
print(points)
ax.scatter(x1, y1)    #  метод, отображающий данные в виде точек
                      #  на плоскости
ax.set(title='Точки')    #  метод, размещающий заголовок
                                       #  над "Axes"
plt.show()


f = d.fill_rips(points1, 2, 3.)
p = d.homology_persistence(f)
dgms = d.init_diagrams(p, f)
d.plot.plot_diagram(dgms[1], labels = True, show = True)
