import math
import numpy as np
import matplotlib.pyplot as plt

rho = 1000.0

x0 = 1100.0
y0 = 1.0

x = np.linspace(1, 1100, 256, endpoint=True)
y = rho*np.log(x/x0)-x+x0+y0

plt.xlim(0, 1200)
plt.ylim(0, 10)
plt.plot(x,y)

plt.show()
