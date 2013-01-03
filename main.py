# coding=utf-8
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from gauss import gauss

import sys

def update_progress(y):
    size = ymax-ymin
    x = int(y-ymin)
    sys.stdout.write("[%s%s] %i%%\r" % ("#"*x, "."*(size-x), x*100/size))
    sys.stdout.flush()


xmin = -20
xmax = 20
ymin = -20
ymax = 20

def plot3D(x, y, f):
    xgrid, ygrid = np.meshgrid(x, y)
    def iterator(x, y):
        update_progress(y[0])
        return map(f, x,y)
    zgrid = map(iterator, xgrid, ygrid)
    fig = plot.figure()
    axes = Axes3D(fig)
    axes.plot_surface(xgrid, ygrid, zgrid)

def intersect(a, b):
    def expr(x,y):
        return gauss(4.5, 4.5, 0, 0, x,y)*gauss(2.5, 3.5, a, b, x,y)
    return integrate.dblquad(expr, -20, 20, lambda x: -20, lambda y: 20)[0]

x = np.arange(xmin, xmax, 1)
y = np.arange(ymin, ymax, 1)

plot3D(x, y, intersect)
plot.show()
