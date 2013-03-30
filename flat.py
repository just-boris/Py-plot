# coding=utf-8
import pylab
import numpy as np
from gauss import GaussX
from planar import PlanarX
from include import coupling

planar = PlanarX(open('matrix/dump1d.csv', 'rb'))
cylinder = GaussX(4.5,4)

def intersect(x):
    cylinder = GaussX(4.5,x)
    return coupling.couplingX(cylinder.func, planar.func)

x = np.arange(-20, 20, 0.1)
pylab.plot(x, map(intersect, x), 'g')

if __name__ == "__main__":
    #только без тестов
    pylab.show()
