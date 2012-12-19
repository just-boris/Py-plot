"""
File            cheney-householder.py
Author        Ernesto P. Adorio, Ph.D.
                  University of the Philippines Extenstion Program at Clark Field
                  Pampanga, the Philippines
Revisions    2009.01.20 first version
References
        Kincaid and Cheney, "Numerical Analysis",  2nd Ed. pp. 299-303
        Brooks Coole Publishing
"""

from math import sqrt
from matlib import *


def cheneyhouseholder(A):
    # Given A, determines a factorization Q A = R or A = Q'R.
    # Remove the verbose print lines if used in a library.
    nrows,  ncols = matdim(A)
    Q = matiden(nrows * nrows)
    R = matiden(nrows * ncols)
    for j in range(nrows -1):
        #compute the column E^2 norm
        X      = [A[p][j] for p in range(j,  nrows)]  # jth column vector.
        Beta= -sqrt(sum(x*x for x in X))
        print "X = ",  X
        print "Beta=",  Beta

        Y    = X[:]
        Y[0] = X[0] - Beta
        print "Y=", Y
        alpha = sqrt(2)/ vecnorm(Y)
        print "alpha=",  alpha

        V = [y * alpha for y in Y]
        print "V=", V
        vvt= matvecvect(V)
        print "vvt:"
        matprint(vvt)

        imvv  = matsub(mateye(len(Y) ),  vvt)
        print "I-vv'"
        matprint (imvv)

        Ui = imvv
        Ui = matprependidentity(Ui,  j)
        print "resolving Ui:"
        print "U_",  j , "= ",
        for u in Ui: print u

        UiA = matprod(Ui,  A)
        print "U_",  j, "A:"
        matprint(UiA)
        A = UiA
        if j == 0:
            Q = Ui
        else:
            Q = matmul(Ui,  Q)
        print "Q:"
        matprint(Q)
        R = UiA
    return Q,  R


if __name__ == "__main__":
    A = [[12, -51, 4],  # Wikipedia
         [6, 167, -68],
         [-4, 24, -41]]

    A = [[63,  41,  -88],      #Cheney
         [42,  60,  51],
         [0, -28,  56],
         [126,  82,  -71]]
    matprint(A)
    Q,  R = cheneyhouseholder(A)
    print "R:"
    matprint(R)
    print("QR:")
    matprint(matmul(Q, A))