import scipy.optimize as opt
from gauss import Gauss
from include import coupling

planarG = (7, 4.5)
cylinderG = (3.5, 3.5)
planar = Gauss(planarG[0], planarG[1], 0, 0)
#function definitions
def intersect(a, b):
    cylinder = Gauss(cylinderG[0], cylinderG[1], a, b)
    return coupling.coupling(planar.gauss, cylinder.gauss)

x, y = opt.fmin_powell(lambda x: -intersect(x[0], x[1]), [1, 2])
print "({0:.3f}, {1:.3f})".format(x, y)