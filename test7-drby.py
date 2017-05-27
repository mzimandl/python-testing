import matplotlib.pyplot as plt

print("model šíření drbů - Daley-Kendall")
print("v populaci je na začátku jedna drbna (y), která zná drb")
print("když se drbna setká s člověkem, který drb nezná (x), předá informaci a udělá z něj také drbnu")
print("když se drbna setká s člověkem co drb zná, drb je považován za zastaralý a přestává drbat, je neaktivní (z)")
print("rovnice:")
print("	dx/dt = -Axy")
print("	dy/dt = Axy - Ayz - Ay(y-1)")
print("	dz/dt = Ayz + Ay(y-1)")
print("A je parametr pravděpodobnosti předání drbu.")

A = 0.001		#parametr pravďěpodobnosti sdělení informace

x0 = 1000.0	#neznají drb
y0 = 1.0		#znají a šíří drb
z0 = 0.0		#znají, ale nešíří drb
t0 = 0.0

dt = 0.1

x = []
y = []
z = []
t = []

x.append(x0)
y.append(y0)
z.append(z0)
t.append(t0)

for i in range (0, 250):
	x.append(x[i] - A*x[i]*y[i]*dt)
	y.append(y[i] + A*(x[i]*y[i]-y[i]*z[i]-y[i]*(y[i]-1))*dt)
	z.append(z[i] + A*(y[i]*z[i]+y[i]*(y[i]-1))*dt)
	t.append(t[i] + dt)

plt.plot(t,x,linewidth=1.5,linestyle="-",label="neznají drb")
plt.plot(t,y,linewidth=1.5,linestyle="-",label="znají a šíří drb")
plt.plot(t,z,linewidth=1.5,linestyle="-",label="znají, ale nešíří drb")

plt.legend(loc='upper left', frameon=True, framealpha=0.8)

plt.show()
