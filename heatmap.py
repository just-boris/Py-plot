# coding=utf-8
import numpy as np
from gauss import Gauss
from planar import Planar
from include import coupling
import pylab
from scipy.optimize import fmin_powell

#function definitions
def intersect(a, b):
    cylinder = Gauss(cylinderG[0], cylinderG[1], a, b)
    return coupling.coupling(planar.func, cylinder.func)

#три функции отрисовки диаграмм
def drawMap(ratio):
    return [[ratio / vmax * planar.func(x, y) for x in range(xmin, xmax + 1)] for y in range(ymin, ymax + 1)]

def buildTable(x, y, ratio):
    return ax.table(
        cellText=[
            [u'Вх. распределение', "%d/%d" % cylinderG],
            [u'Вых. распределение', "%d/%d" % (7,7)],
            [u'Точка пересечения', "(%.2f, %.2f)" % (x, y)],
            [u'К-т передачи', "%.4f" % ratio],
            [u'Макс. к-т передачи', "%.4f" % maxRatio]
        ],
        loc='upper center'
    )

def buildShape(G, a, b):
    t = np.arange(0, 2 * np.pi + 0.1, 0.1)
    return G[0] * np.cos(t) + a, G[1] * np.sin(t) + b

#настройки matplotlib
gridShape = (2, 2)
pylab.rc('font', **{'family': 'serif'})

#объявление наших условий
#TODO перенести в конфигурационный файл
xmin = -20
xmax = 20
ymin = -20
ymax = 20
planarG = (4.6, 4)
cylinderG = (3, 3)
planar = Planar(open('matrix/dump2d.csv', 'rb'))
planarMax = fmin_powell(lambda x: -planar.func(*x), [0, -1])
vmax = planar.func(*planarMax)
initPoint = fmin_powell(lambda x: -intersect(*x), [1, 2])
ratio = maxRatio = intersect(*initPoint)

#верхняя половина - слева
pylab.subplot2grid(gridShape, (0, 0), adjustable='box', aspect=1)
p = pylab.imshow(drawMap(ratio), extent=[xmin, xmax, ymin, ymax], vmax=1, origin="lower")
point = pylab.plot(initPoint[0], initPoint[1], 'b+')
pylab.colorbar()

#обработка клика
def OnClick(event):
    x = event.xdata
    y = event.ydata
    if x is None or y is None:
        return
    ratio = intersect(x, y)
    p.set_data(drawMap(ratio))
    point[0].set_data(x, y)
    table[0].remove()
    table[0] = buildTable(x, y, ratio)
    X, Y = buildShape(cylinderG, x, y)
    line[0].set_data(X, Y)
    pylab.show()

fig = pylab.gcf()
cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)

#верхняя половина - справа
ax = pylab.subplot2grid(gridShape, (0, 1), adjustable='box', aspect=1)
# x, y = buildShape(planarG, 0, 0)
# pylab.plot(x, y, 'k')
x, y = buildShape(cylinderG, 0, 0)
line = pylab.plot(x, y, 'b')
pylab.axis([-20, 20, -20, 20])
#нижняя половина - справа
ax = pylab.subplot2grid(gridShape, (1, 0), colspan=2, frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
table = [buildTable(*initPoint, ratio=ratio)]

if __name__ == "__main__":
    #собираем все вместе
    pylab.show()
else:
    #результаты теста
    print "planarMax: ({0:.3f}, {1:.3f})".format(*planarMax)
    print "couplingMax: ({0:.3f}, {1:.3f})".format(*initPoint)


