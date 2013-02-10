import pylab
import scipy.integrate as integrate
import numpy as np
from gauss import GaussX
from include import coupling

planar = GaussX(7,0)
cylinder = GaussX(4.5,4)
def intersect_old(x):
    cylinder = GaussX(4.5,x)
    def expr(x):
        return min(planar.gauss(x), cylinder.gauss(x))
    return integrate.quad(expr, -20, 20)[0]
def intersect_new(x):
    cylinder = GaussX(4.5,x)
    return coupling.couplingX(cylinder.gauss, planar.gauss)

x = np.arange(-20, 20, 0.1)
pylab.plot(x, map(intersect_old, x), 'g')
pylab.plot(x, map(intersect_new, x), 'r')

pylab.show()