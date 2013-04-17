import math
import numpy as np
import pylab
from include.coupling import coupling
from planar import Planar
from gauss import Gauss

planar = Planar(open('matrix/dump2d.csv'))
w = (3, 3)
lam = 1.55
n = 1.47
divergence_angle = [math.atan(lam/(math.pi*n*width)) for width in w]

def get_angle(d, w, theta):
    return w + 2*d*math.tan(math.atan(theta))

def divergence(w, d):
    return (get_angle(d, w, theta) for w, theta in zip(w, divergence_angle))

def traversal(d):
    w1 = divergence(w, d)
    cylinder = Gauss(*w1, a=0, b=-2.98)
    return coupling(planar.func, cylinder.func)


x = np.arange(0, 20, 0.1)
pylab.plot(x, map(traversal, x), 'g')
pylab.show()