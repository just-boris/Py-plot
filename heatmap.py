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
vmax = planar.gauss(0,0)
ratio = intersect(0,0)
print ratio
p = plt.imshow([[ratio*planar.gauss(x, y) for x in range(xmin, xmax)] for y in range(ymin, ymax)], extent=[xmin, xmax, ymin, ymax],vmax=vmax)
plt.colorbar()
plt.show()

