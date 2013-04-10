import scipy.optimize as opt
from gauss import Gauss
from planar import Planar
from include import coupling

planarG = (7, 4.5)
cylinderG = (3.5, 3.5)
planar = Planar(open('matrix/dump2d.csv', 'rb'))
#function definitions
def intersect(a, b):
    cylinder = Gauss(cylinderG[0], cylinderG[1], a, b)
    return coupling.coupling(planar.func, cylinder.func)

x, y = opt.fmin_powell(lambda x: -planar.func(x[0], x[1]), [0, -1])
print "({0:.3f}, {1:.3f})".format(x, y)