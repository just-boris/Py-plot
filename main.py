# coding=utf-8
import numpy as np
import scipy.integrate as integrate
import plot3D
from gauss import Gauss

xmin = -20
xmax = 20
ymin = -20
ymax = 20

planar = Gauss(4.5, 4.5, 0, 0)

def intersect(a, b):
    cylinder = Gauss(4.5, 4.5, a, b)
    def expr(x,y):
        return min(planar.gauss(x,y), cylinder.gauss(x,y))
    return integrate.dblquad(expr, -20, 20, lambda x: -20, lambda y: 20)[0]

x = np.arange(xmin, xmax, 1)
y = np.arange(ymin, ymax, 1)

plot3D.doPlot(x, y, intersect)