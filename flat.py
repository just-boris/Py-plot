import pylab
import scipy.integrate as integrate
import numpy as np
from gauss import GaussX

planar = GaussX(7,-4)
cylinder = GaussX(4.5,4)
def substrat(x):
    cylinder = GaussX(4.5,x)
    def expr(x):
        return min(planar.gauss(x), cylinder.gauss(x))
    return integrate.quad(expr, -20, 20)[0]

x = np.arange(-20, 20, 0.1)
y1 = map(planar.gauss, x)
y2 = map(cylinder.gauss, x)
pylab.plot(x, y1, 'g')
pylab.plot(x, y2, 'r')
pylab.fill(x,np.minimum(y1,y2), hatch='\\', color='w')
pylab.show()