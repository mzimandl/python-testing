import math
import numpy as np
import matplotlib.pyplot as plt

g = -9.81
t = 1

x0 = 0.0
y0 = 0.0

vx0 = 5.0
vy0 = 50.0

x = []
y = []

x.append(x0+vx0*t)
y.append(x0+vx0*t)

vx = vx0
vy = vy0

for i in range (0, 10):
	vy = vy + g*t
	x.append(x[i]+vx*t)
	y.append(y[i]+vy*t)
	print(i)

plt.plot(x,y)
plt.show()
