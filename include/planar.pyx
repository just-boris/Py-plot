import csv
cdef extern from "math.h":
    float sin(float args)
    float sqrt(float args)
    double M_PI

cdef int MIN_X = - 20, MIN_Y = -20, MAX_X = 20, MAX_Y = 20
def fi_p(int k, float x):
    nr = 1 / sqrt((MAX_Y - MIN_Y)/2)
    return nr * sin((k + 1) * M_PI * (x - MIN_Y)/(MAX_Y - MIN_Y))
cdef class Planar:
    def __init__(self):
        pass
    def planar(self, float x, float y):
        pass

class PlanarX():
    def __init__(self, csv_file):
        self.HE = [[float(item) for item in row] for row in csv.reader(csv_file)]

    def mode_func(self, int m, double x):
        def iterator(a, item):
            return a+item[1]*fi_p(item[0], x)
        row = enumerate(self.HE[(-1-m)], 0)
        return reduce(iterator, row, 0)
    def planar(self, double x):
        return self.mode_func(0, x)