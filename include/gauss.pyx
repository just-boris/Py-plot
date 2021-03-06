cdef extern from "math.h":
    float exp(float args)
    float sqrt(float args)
    double M_PI
cdef class Gauss:
    cdef double A, X, Y, a, b
    def __init__(self, s1, s2, a, b):
        self.X = 2*s1**2
        self.Y = 2*s2**2
        self.a = a
        self.b = b
    def func(self, float x, float y):
        return exp(-(x-self.a)**2/self.X-(y-self.b)**2/self.Y)

cdef class GaussX:
    cdef double A, X, a
    def __init__(self, s1, a):
        self.X = 2*s1**2
        self.a = a
    def func(self, float x):
        return exp(-(x-self.a)**2/self.X)