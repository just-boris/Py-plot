# coding=utf-8
# coding=utf-8
import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

xmin = -20
xmax = 20
ymin = -20
ymax = 20

def update_progress(y):
    size = ymax-ymin
    x = int(y-ymin)
    sys.stdout.write("[%s%s] %i%%\r" % ("#"*x, "."*(size-x), x*100/size))
    sys.stdout.flush()
def doPlot(x, y, f):
    xgrid, ygrid = np.meshgrid(x, y)
    def iterator(x, y):
        update_progress(y[0])
        return map(f, x,y)
    zgrid = map(iterator, xgrid, ygrid)
    fig = plot.figure()
    axes = Axes3D(fig)
#если нужна опорная линия - раскомментить
#    axes.plot3D([0,0], [0,0], [0,0.01])
    axes.plot_surface(xgrid, ygrid, zgrid, rstride=1, cstride=1)
    plot.show()
