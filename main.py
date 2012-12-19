# coding=utf-8
import numpy as np
import pylab
import matplotlib.pyplot as plot
import matplotlib.mlab as mlab
import func

def nRef(x, ncover = 1,  nsubstrat = 1.5, nmax = 1.6):
    if x > 0:    return ncover
    elif x > -2: return nsubstrat
    else:        return nmax

#physics
lam = 1.0
klam = 2*np.pi/lam
#math
HE_range = 80
#geometry
xMin = -3
xMax = 3
xDelta = 0.01

nr = 1/np.sqrt((xMax-xMin)/2)

def HE_func(i,j):
    if j == 30: print i
    if j >= i: return 0
    fi_p_list = [fi_p(j-1, x) for x in xList]
    return sum([fi_p_list[index]*(fid2_p(i-1, x) + (klam*nRef(x))**2 * fi_p_list[index]) for index, x in enumerate(xList)])*xDelta
xList = mlab.frange(xMin, xMax, xDelta)

HE = [[HE_func(i,j) for j in range(1, HE_range+1)] for i in range(1, HE_range+1)]

#yList = [nRef(x) for x in xList]
#plot.plot(xList, yList)
#
#yList = []
#plot.show()