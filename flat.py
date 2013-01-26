import pylab
import scipy.integrate as integrate
import numpy as np
from gauss import GaussX

planar = GaussX(4.5,0)

def substrat(x):
    cylinder = GaussX(4.5,x)
    def expr(x):
        return min(planar.gauss(x), cylinder.gauss(x))
    return integrate.quad(expr, -20, 20)[0]

x = np.arange(-20, 20, 0.1)

pylab.plot(x, map(substrat, x), 'o')
pylab.show()