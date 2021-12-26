from numpy import *
import matplotlib.pyplot as plt
dt = 0.001
R=10
h=R
u=0
t=0
g=10
Tps=[]
Hps=[]
while t<5:
    Dh=R-h
    a=-g*sqrt(R**2-Dh**2)/R
    u+=a*dt
    h+=u*dt
    Tps.append(t)
    Hps.append(h)
    t+=dt
plt.plot(Tps,Hps)