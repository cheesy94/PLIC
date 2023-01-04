# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:07:08 2022

@author: carmomo4
"""

from PLIC import get_interface_2D
import numpy as np
import matplotlib.pyplot as plt


### SIMPLE TEST

# cell vof
c = 0.7

# normal vector
n = (0.2, 0.4)

# cell size
xcoords = (0,1)
ycoords = (2,3)

xx,yy = get_interface_2D(c,n,xcoords,ycoords)

plt.figure()
plt.plot(xx,yy)
plt.xlim(xcoords)
plt.ylim(ycoords)


### IMAGE TEST
gridsize = (3,3)

# cells vof
c = np.array([1,1,0.18,#0,
              1,0.86,0.015,#0,
              0.7,0.15,0])#,0,
              #0,0,0,0])

# normal vectors assignment
#n = np.array([(),(),(0.1,0.9),
#               (),(0.4,0.6),(0.3,0.7),
#               (0.8,0.2),(0.5,0.5),()],dtype=object)

# normal vectors calculation from vof field
nx,ny = np.gradient(-c.reshape(gridsize))
#nx[(0,-1),:] /= 2
#ny[:,(0,-1)] /= 2
n = np.stack((nx.ravel(),ny.ravel()), axis=1)

# cell sizes
xc = np.linspace(0,0+gridsize[0],gridsize[0]+1)
yc = np.linspace(1,1+gridsize[1],gridsize[1]+1)
xcoords,ycoords = np.meshgrid(xc,yc,indexing='ij')

xx = np.empty((2,c.size))
xx[:] = np.nan
yy = np.empty((2,c.size))
yy[:] = np.nan

for e in range(c.size):
    if c[e]>=1 or c[e]<=0:
        continue
        
    i = int(e/gridsize[1])
    j = e%gridsize[1]
    xx[:,e],yy[:,e] = get_interface_2D(c[e],n[e],xc[i:i+2],yc[j:j+2])
    
plt.figure()
plt.plot(xx,yy,'k--')
plt.xlim(xc.min(),xc.max())
plt.ylim(yc.min(),yc.max())
plt.gca().set_xticks(xc)
plt.gca().set_yticks(yc)
plt.grid(which='major')
