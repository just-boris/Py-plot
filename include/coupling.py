import scipy.integrate as integrate

def coupling(input, out):
    A = integrate.dblquad(lambda x,y: input(x,y)*out(x,y), -20, 20, lambda x: -20, lambda y: 20)[0]
    B = integrate.dblquad(lambda x,y: input(x,y)**2, -20, 20, lambda x: -20, lambda y: 20)[0]
    C = integrate.dblquad(lambda x,y: out(x,y)**2, -20, 20, lambda x: -20, lambda y: 20)[0]
    return A*A/B/C

def couplingX(input, out):
    A = integrate.quad(lambda x: input(x)*out(x), -20, 20)[0]
    B = integrate.quad(lambda x: input(x)**2, -20, 20)[0]
    C = integrate.quad(lambda x: out(x)**2, -20, 20)[0]
    return A*A/B/C