import math
import numpy as np
import matplotlib.pyplot as plt

#pocet kraliku a lisek v rovnováze, kdy se populace s časem nemění
x0 = 100.0
y0 = 40.0
#porucha poctu kraliku od rovnovahy
K = 150

a = 4.0 #rychlost mnozeni kraliku
c = 0.2 #rychlost uhynu lisek
b = a/y0 #ubytek kraliku lovem, výpočet z rovnovážného počtu
h = c/x0 #prirustek lisek lovem kraliku, výpočet z rovnovážného počtu

print("Systém predátor-kořist se řídí rovnicemi modelu Lotka-Volterra")
print("králíci x:	dx/dt = ax - bxy")
print("lišky y:	dy/dt = -cy + hxy")

print("rychlost množení králíků:	a = ", a)
print("úbytek králíků lovem:		b = ", b)
print("úhyn lišek:			c = ", c)
print("množení lišek podpořený lovem:	h = ", h)

N = 1000 #pocet bodů v grafu
last = 20.0 #konečný čas
t = last/N #časový interval

#analytické poruchové řešení, !systém musí být poblíž rovnováhy x0, y0; K musí být malé!
X = np.linspace(0, last, N, endpoint=True)
C,S = c/h + K*np.cos(math.sqrt(a*c)*X), a/b + (h/b)*math.sqrt(a/c)*K*np.sin(math.sqrt(a*c)*X)

#numerické řešení diferenciálních rovnic Lotky-Volterry
kralik = []
liska = []

kralik.append(x0+K)
liska.append(y0)
for i in range (0, N-1):
	kralik.append(kralik[i]+(a*kralik[i]-b*kralik[i]*liska[i])*t)
	liska.append(liska[i]+(-c*liska[i]+h*kralik[i]*liska[i])*t)	

#vykreslení grafu
plt.plot(X,kralik,linewidth=1.5,linestyle="-",label="králíci numericky")
plt.plot(X,liska,linewidth=1.5,linestyle="-",label="lišky numericky")

plt.plot(X,C,linewidth=1.5,linestyle="--",label="králíci analyticky")
plt.plot(X,S,linewidth=1.5,linestyle="--",label="lišky analyticky")

plt.plot([0,last],[0,0],color="black")

plt.legend(loc='upper left', frameon=True, framealpha=0.8)

plt.show()
