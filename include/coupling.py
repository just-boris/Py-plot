import numpy as np
import scipy.integrate as integrate

def simps_dblquad(func, a, b, gfun, hfun):
    def _infunc(x,func,gfun,hfun):
        a = gfun(x)
        b = hfun(x)
        return integrate.simps([func(x, y) for y in np.arange(a, b, 0.1)],dx=0.1)
    return integrate.simps([_infunc(x, func,gfun, hfun) for x in np.arange(a, b, 0.1)],dx=0.1)

def coupling(input, out):
    A = simps_dblquad(lambda x,y: input(x,y)*out(x,y), -20, 20, lambda x: -20, lambda y: 20)
    B = simps_dblquad(lambda x,y: input(x,y)**2, -20, 20, lambda x: -20, lambda y: 20)
    C = simps_dblquad(lambda x,y: out(x,y)**2, -20, 20, lambda x: -20, lambda y: 20)
    return A*A/B/C

def couplingX(input, out):
    A = integrate.quad(lambda x: input(x)*out(x), -20, 20)[0]
    B = integrate.quad(lambda x: input(x)**2, -20, 20)[0]
    C = integrate.quad(lambda x: out(x)**2, -20, 20)[0]
    return A*A/B/C