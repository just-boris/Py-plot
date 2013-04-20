import numpy as np
from include.plot3D import doPlot
from planar import Planar
import pylab

xmin = -7
xmax = 7
ymin = -7
ymax = 7

use3d = True

planar = Planar(open('matrix/dump2d.csv', 'rb'))

def drawMap():
    return [[planar.func(x, y) for x in range(xmin, xmax+1)] for y in range(ymin, ymax+1)]

x = np.arange(xmin, xmax+1, 0.3)
y = np.arange(ymin, ymax+1, 0.3)

if use3d:
    doPlot(x, y, lambda x,y: planar.func(x,y))
else:
    CS = pylab.contour(x, y, drawMap(), 10, colors='k')
    pylab.clabel(CS, fontsize=9, inline=1)
    pylab.show()


