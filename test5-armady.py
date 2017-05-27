import math
import numpy as np
import matplotlib.pyplot as plt

x0 = 600.0
a = 0.01

y0 = 500.0
b = 0.02

k = np.sqrt(a*b)

t = np.linspace(0, 100, 256, endpoint=True)

plt.ylim(0, 600)

x = x0*np.cosh(k*t) - np.sqrt(b/a)*y0*np.sinh(k*t)
y = y0*np.cosh(k*t) - np.sqrt(a/b)*x0*np.sinh(k*t)

plt.plot(t,x)
plt.plot(t,y)

plt.show()
