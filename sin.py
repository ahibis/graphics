from numpy import *
import matplotlib.pyplot as plt
u=arange(-10,10,0.1);
v=arange(-10,10,0.1);
x, y = meshgrid(u,v)
z= sin(x+y*1j).real
z1= sin(x+y*1j).imag
ax = plt.subplot(211,projection='3d')
ax1 = plt.subplot(212,projection='3d')

ax.plot_surface(x,y,z, cmap='plasma');
ax1.plot_surface(x,y,z1, cmap='plasma');