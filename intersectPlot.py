# coding=utf-8
import numpy as np
import plot3D
from gauss import Gauss

xmin = -20
xmax = 20
ymin = -20
ymax = 20

planar = Gauss(4.5, 4.5, 0, 0)
cylinder = Gauss(4.5, 4.5, 0, 0)
def expr(x,y):
    return min(planar.gauss(x,y), cylinder.gauss(x,y))

x = np.arange(xmin, xmax, 1)
y = np.arange(ymin, ymax, 1)
plot3D.doPlot(x,y,expr)
