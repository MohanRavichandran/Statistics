
"""
import numpy as np
import matplotlib.pyplot as plt


a = [float(k)*.0001 for k in range(-100,100)]
a[100]=1
b = [x + 2*(x**2)*np.sin(1/x) for x in a]
b[100]=0
fig = plt.figure()
plt.plot(b)
plt.show()
"""
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')


t  = np.linspace(1, 200, 1000)

x = [1/float(a)*np.cos(a) for a in t]
y = [1/float(a)*np.sin(a) for a in t]
ax.plot(x, y, label='parametric curve')
ax.legend()
'''
r  = np.linspace(-20, 20, 1000)
x = np.sin(r)
y = np.cos(r)
ax.plot(x, y,5*r, label='parametric curve')
ax.legend()
'''


plt.show()

