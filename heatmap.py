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

planarG1 = 4.5
planarG2 = 4.5
cylinderG1 = 4.5
cylinderG2 = 4.5
planar = Gauss(planarG1, planarG1, 0, 0)
vmax = planar.gauss(0,0)

pylab.subplot2grid (gridShape, (0, 0), colspan = 2, rowspan = 2)
def intersect(a, b):
    cylinder = Gauss(cylinderG1, cylinderG2, a, b)
    def expr(x,y):
        return min(planar.gauss(x,y), cylinder.gauss(x,y))
    return integrate.dblquad(expr, xmin, xmax, lambda x: ymin, lambda x: ymax)[0]

def drawMap(a, b):
    ratio = intersect(a,b)
    print ratio
    return [[ratio/vmax*planar.gauss(x, y) for x in range(xmin, xmax+1)] for y in range(ymin, ymax+1)]
def getCellData(x,y):
    return [
        ["%s/%s"%(planarG1, planarG2)],
        ["%s/%s"%(cylinderG1, cylinderG2)],
        ["(%.4s, %.4s)"%(x, y)]
    ]
def buildTable(cells):
    ax.table(
        rowLabels=[u'Планарный', u'Цилиндрический', u'Точка пересечения'],
        cellText=cells,
        loc='center'
    )
p = pylab.imshow(drawMap(0,0), extent=[xmin, xmax, ymin, ymax])
point = pylab.plot(0,0, 'b+')
def OnClick(event):
    x = event.xdata
    y = event.ydata
    p.set_data(drawMap(x, y))
    point[0].set_data(x, y)
    buildTable(getCellData(x,y))
    pylab.show()
fig = pylab.gcf()

cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)
pylab.colorbar()

ax = pylab.subplot2grid (gridShape, (2, 1), frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
buildTable(getCellData(0,0))
pylab.show()


