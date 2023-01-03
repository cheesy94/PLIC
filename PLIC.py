# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 01:56:13 2021

@author: Cheesy94
"""

import numpy as np

def get_interface_2D(c,b,x,y):
    Dx = np.diff(x)[0]
    Dy = np.diff(y)[0]
    
    vof = 0.5-abs(0.5-c)
    dx = np.sqrt(2*abs(b[1]/b[0])*vof*Dx*Dy)
    dy = -b[0]/b[1]*min(dx,Dx)
    
    if dx>Dx:
        #caso b
        xx = x
        
        vof = 0.5-b[1]*(0.5-c)/abs(b[1])
        y2 = vof*Dy-Dx/2*b[0]/b[1]+y[0]
        yy = np.array([y2-dy,y2])
        
    elif abs(dy)>Dy:
        #caso c
        dx = -b[1]/b[0]*Dy
        yy = y
        
        vof = 0.5-b[0]*(0.5-c)/abs(b[0])
        x2 = vof*Dx-Dy/2*b[1]/b[0]+x[0]
        xx = np.array([x2-dx,x2])
        
    else:
        #caso a
        if (c-0.5)*(b[0])<0:
            xx = np.array([x[0],x[0]+dx])
            yy = np.array([-dy, 0])
        else:
            xx = np.array([x[1]-dx,x[1]])
            yy = np.array([0, dy])
            
        if (c-0.5)*(b[1])<0:
            yy += y[0]
        else:
            yy += y[1]
        
    return (xx,yy)
