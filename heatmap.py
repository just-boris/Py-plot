# coding=utf-8
from gauss import Gauss
from planar import Planar
import platform
from include import coupling
import pylab
from scipy.optimize import fmin_powell

#function definitions
def intersect(a, b):
    cylinder = Gauss(cylinderG[0], cylinderG[1], a, b)
    return coupling.coupling(planar.func, cylinder.func)

def getFontName():
    if platform.system() == 'Windows':
        return 'arial'
    else:
        return 'serif'

#три функции отрисовки диаграмм
def drawMap(ratio):
    return [[ratio / vmax * planar.func(x, y) for x in range(xmin, xmax + 1)] for y in range(ymin, ymax + 1)]

def buildTable(x, y, ratio):
    return ax.table(
        cellText=[
            [u'Радиус моды волокна, мкм', "%.2f" % cylinderG[0]],
            [u'Координаты центра волокна, (мкм, мкм)', "(%.2f, %.2f)" % (x, y)],
            [u'К-т передачи', "%.4f" % ratio],
            [u'Макс. к-т передачи', "%.4f" % maxRatio]
        ],
        loc='upper center'
    )

def buildCylinder(a, b):
    cylinder = Gauss(cylinderG[0], cylinderG[1], a, b)
    return [[cylinder.func(x, y) for x in range(xmin, xmax + 1)] for y in range(ymin, ymax + 1)]

def buildContours(x, y):
    contours.cla()
    xmap = range(xmin, xmax + 1)
    ymap = range(ymin, ymax + 1)
    contours.contour(xmap, ymap, drawMap(vmax), (0.1, ), colors='k')
    contours.contour(xmap, ymap, buildCylinder(x,y), (0.55, ), colors='b')
    contours.set_xlabel(u'x, мкм')
    contours.set_ylabel(u'y, мкм')

#настройки matplotlib
gridShape = (2, 2)
pylab.rc('font', **{'family': getFontName(), 'size'  : 14})
pylab.rcParams['toolbar'] = 'None'
pylab.rcParams['figure.figsize'] = 12, 8
pylab.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.01)

#объявление наших условий
#TODO перенести в конфигурационный файл
xmin = -10
xmax = 10
ymin = -10
ymax = 10
cylinderG = (4.65, 4.65)
planar = Planar(open('matrix/dump2d.csv', 'rb'))
planarMax = fmin_powell(lambda x: -planar.func(*x), [0, -1])
vmax = planar.func(*planarMax)
initPoint = fmin_powell(lambda x: -intersect(*x), [1, 2])
ratio = maxRatio = intersect(*initPoint)

#верхняя половина - слева
ax = pylab.subplot2grid(gridShape, (0, 0), adjustable='box', aspect=1)
p = pylab.imshow(drawMap(ratio), extent=[xmin, xmax, ymin, ymax], vmax=1, origin="lower")
ax.set_xlabel(u'x, мкм')
ax.set_ylabel(u'y, мкм')
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
    table[0].auto_set_font_size(False)
    table[0].set_fontsize(14)
    table[0].scale(1, 2)
    buildContours(x, y)
    pylab.show()

fig = pylab.gcf()
cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)

#верхняя половина - справа
contours = pylab.subplot2grid(gridShape, (0, 1), adjustable='box', aspect=1)
buildContours(*initPoint)
#нижняя половина - справа
ax = pylab.subplot2grid(gridShape, (1, 0), colspan=2, frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
table = [buildTable(*initPoint, ratio=ratio)]
table[0].auto_set_font_size(False)
table[0].set_fontsize(14)
table[0].scale(1, 2)

if __name__ == "__main__":
    #собираем все вместе
    pylab.gcf().canvas.set_window_title('Coupling Plot')
    pylab.show()
else:
    #результаты теста
    print "planarMax: ({0:.3f}, {1:.3f})".format(*planarMax)
    print "couplingMax: ({0:.3f}, {1:.3f})".format(*initPoint)


