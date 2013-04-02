import numpy as np
import scipy.integrate as integrate

X_INTERVAL = 0.5
xmin = ymin = -20
xmax = ymax = 20

def simps_dblquad(func, a, b, gfun, hfun):
    def _infunc(x,func,gfun,hfun):
        a = gfun(x)
        b = hfun(x)
        return integrate.simps([func(x, y) for y in np.arange(a, b, X_INTERVAL)],dx=X_INTERVAL)
    return integrate.simps([_infunc(x, func,gfun, hfun) for x in np.arange(a, b, X_INTERVAL)],dx=X_INTERVAL)

def coupling(input, out):
    A = simps_dblquad(lambda x,y: input(x,y)*out(x,y), xmin, xmax, lambda x: ymin, lambda y: ymax)
    B = simps_dblquad(lambda x,y: input(x,y)**2, xmin, xmax, lambda x: ymin, lambda y: ymax)
    C = simps_dblquad(lambda x,y: out(x,y)**2, xmin, xmax, lambda x: ymin, lambda y: ymax)
    return A*A/B/C

def couplingX(input, out):
    A = integrate.quad(lambda x: input(x)*out(x), xmin, xmax)[0]
    B = integrate.quad(lambda x: input(x)**2, xmin, xmax)[0]
    C = integrate.quad(lambda x: out(x)**2, xmin, xmax)[0]
    return A*A/B/C