# coding=utf-8
import numpy as np
from gauss import Gauss
from include import plot3D, coupling

xmin = -20
xmax = 20
ymin = -20
ymax = 20

planar = Gauss(4.5, 4.5, 0, 0)

def intersect(a, b):
    cylinder = Gauss(4.5, 4.5, a, b)
    return coupling.coupling(planar.func, cylinder.func)

x = np.arange(xmin, xmax, 1)
y = np.arange(ymin, ymax, 1)

plot3D.doPlot(x, y, intersect)