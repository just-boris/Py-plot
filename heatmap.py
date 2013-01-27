import scipy.integrate as integrate
import numpy as np
from gauss import Gauss
import matplotlib.pyplot as plt

xmin = -20
xmax = 20
ymin = -20
ymax = 20

planar = Gauss(4.5, 4.5, 0, 0)

def intersect(a, b):
    cylinder = Gauss(2, 2, a, b)
    def expr(x,y):
        return min(planar.gauss(x,y), cylinder.gauss(x,y))
    return integrate.dblquad(expr, xmin, xmax, lambda x: ymin, lambda x: ymax)[0]

def drawMap(a, b):
    ratio = intersect(a,b)
    print ratio
    return [[ratio*planar.gauss(x, y) for x in range(xmin, xmax+1)] for y in range(ymin, ymax+1)]

vmax = planar.gauss(0,0)
p = plt.imshow(drawMap(0,0), extent=[xmin, xmax, ymin, ymax],vmax=vmax)
point = plt.plot(0,0, 'b+')
def OnClick(event):
    p.set_data(drawMap(event.xdata, event.ydata))
    point[0].set_data(event.xdata, event.ydata)
    plt.show()
fig = plt.gcf()
plt.clim()
cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)
plt.colorbar()
plt.show()

