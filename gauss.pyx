pi = 3.1415
cdef extern from "math.h":
    float exp(float args)
def gauss(float s1, float s2, float a, float b, float x, float y):
    return 1/(2*pi)*s1*s2*exp(-(x-a)**2/(2*s1**2)-(y-b)**2/(2*s2**2))