import pylab
import scipy.integrate as integrate
import numpy as np
from gauss import Gauss

planar = Gauss(4.5,4.5,0,0)

def substrat(x):
    cylinder = Gauss(4.5,4.5,x,0)
    def expr(x,y):
        return min(planar.gauss(x,y), cylinder.gauss(x,y))
    return integrate.dblquad(expr, -20, 20, lambda x: -20, lambda y: 20)[0]

x = np.arange(-20, 20, 0.1)

pylab.plot(x, map(substrat, x), 'o')
pylab.show()