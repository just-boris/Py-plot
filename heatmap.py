# coding=utf-8
import scipy.integrate as integrate
import numpy as np
from gauss import Gauss
import pylab

gridShape = (3,2)
pylab.rc('font',**{'family':'verdana'})

xmin = -20
xmax = 20
ymin = -20
ymax = 20

planarG = (7,4.5)
cylinderG = (3.5,3.5)
planar = Gauss(planarG[0], planarG[1], 0, 0)
vmax = planar.gauss(0,0)

pylab.subplot2grid (gridShape, (0, 0), colspan = 2, rowspan = 2)
def intersect(a, b):
    cylinder = Gauss(cylinderG[0], cylinderG[1], a, b)
    def expr(x,y):
        return min(planar.gauss(x,y), cylinder.gauss(x,y))
    return integrate.dblquad(expr, xmin, xmax, lambda x: ymin, lambda x: ymax)[0]

def drawMap(a, b):
    ratio = intersect(a,b)
    print ratio
    return [[ratio/vmax*planar.gauss(x, y) for x in range(xmin, xmax+1)] for y in range(ymin, ymax+1)]
def getCellData(x,y):
    return [
        [u'Планарный', "%s/%s"%planarG],
        [u'Цилиндрический', "%s/%s"%cylinderG],
        [u'Точка пересечения', "(%.4s, %.4s)"%(x, y)]
    ]
def buildTable(cells):
    return ax.table(
        cellText=cells,
        loc='upper center'
    )
def buildShape(G, a, b):
    t = np.arange(0, 2*np.pi+0.1, 0.1)
    return (G[0]*np.cos(t)+a, G[1]*np.sin(t)+b)
p = pylab.imshow(drawMap(0,0), extent=[xmin, xmax, ymin, ymax], vmax=1)
point = pylab.plot(0,0, 'b+')
def OnClick(event):
    x = event.xdata
    y = event.ydata
    p.set_data(drawMap(x, y))
    point[0].set_data(x, y)
    table[0].remove()
    table[0] = buildTable(getCellData(x,y))
    X,Y=buildShape(cylinderG,x,y)
    line[0].set_data(X,Y)
    pylab.show()
fig = pylab.gcf()

cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)
pylab.colorbar()
ax = pylab.subplot2grid (gridShape, (2, 0))
x,y = buildShape(planarG,0,0)
pylab.plot(x,y, 'k')
x,y = buildShape(cylinderG,0,0)
line = pylab.plot(x,y, 'b')

ax = pylab.subplot2grid (gridShape, (2, 1), frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
table = [buildTable(getCellData(0,0))]
pylab.show()


