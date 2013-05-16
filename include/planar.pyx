import csv
cdef extern from "math.h":
    float sin(float args)
    float sqrt(float args)
    double M_PI

class Planar:
    def __init__(self, csv_file):
        self.maxVal = 0.141867
        self.MIN_C = -10; self.MIN_Z = -10
        self.MAX_C = 10; self.MAX_Z = 10
        self.Nf = 36
        self.NNz = 16
        self.NNc = 16
        self.Nh = 2

        self.HE = [[float(item) for item in row] for row in csv.reader(csv_file)]

        self.ch = float(self.MAX_C-self.MIN_C)/((self.NNc+1)*self.Nf)
        self.zh = float(self.MAX_Z-self.MIN_Z)/((self.NNz+1)*self.Nf)
        self.zcN = [[1, 1/(self.ch*self.Nf)], [1/(self.zh*self.Nf), 1/(self.zh*self.ch*self.Nf*self.Nf)]]

    def fi(self, int k, float x):
        x = x/self.Nf-1
        if abs(x) > 1:
            return 0
        if x >= 0:
            a = 1 - x
            if k == 0:
                b = 1 + 2 * x
            else:
                b = x
        else:
            a = 1 + x
            if k == 0:
                b = 1 - 2 * x
            else:
                b = x
        return a * a * b
    def mode_func(self, int m, float c, float z):
        iz = int((z - self.MIN_Z) / self.zh) #if (iz >= iiz)iz = iiz - 1;
        ic = int((c - self.MIN_C) / self.ch) #if (ic >= iic)ic = iic - 1;
        return self.mode_func_idx(m, ic, iz)

    def mode_func_idx(self, int m, int idx_c, int idx_z):
        row = self.HE[(-1-m)]
        result = float(0)
        j = int(idx_c / self.Nf) - 1
        i = int(idx_z / self.Nf) - 1
        for zh in range(2):
            for ch in range(2):
                for m in range(2):
                    for n in range(2):
                        l = ch+(n + j)*2+zh*self.NNc*2+(m + i)*self.NNc*4
                        if 0 <= l < len(self.HE):
                            result += self.fi(zh, idx_z - (i + m) * self.Nf) \
                                      * self.fi(ch, idx_c - (j + n) * self.Nf) \
                                      * row[l] * self.zcN[zh][ch]
        return result

    def func(self, float x, float y):
        if self.MIN_C < x < self.MAX_C and self.MIN_Z < y < self.MAX_Z:
            return -self.mode_func(0, x, y)/self.maxVal
        else:
            return 0

class PlanarX:
    def __init__(self, csv_file):
        self.maxVal = 0.582845
        self.MIN_X = self.MIN_Y = -20
        self.MAX_X = self.MAX_Y = 20
        self.HE = [[float(item) for item in row] for row in csv.reader(csv_file)]

    def fi_p(self, int k, float x):
        nr = 1 / sqrt((self.MAX_Y - self.MIN_Y)/2)
        return nr * sin((k + 1) * M_PI * (x - self.MIN_Y)/(self.MAX_Y - self.MIN_Y))

    def mode_func(self, int m, double x):
        def iterator(a, item):
            return a+item[1]*self.fi_p(item[0], x)
        row = enumerate(self.HE[(-1-m)], 0)
        return reduce(iterator, row, 0)
    def func(self, double x):
        return self.mode_func(0, x)/self.maxVal