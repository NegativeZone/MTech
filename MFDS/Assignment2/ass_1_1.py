import numpy as np
import math

def round_sig(x, d=4):
    if x == 0:
        return x
    return round(x, d - math.floor(math.log10(abs(x))))

def frobenius(m, n):
    A = np.random.rand(m,n)
    for i in range(0, m):
        for j in range(0, n):
            while A[i, j] < 1:
                A[i, j] = A[i, j] * 10
            A[i, j] = round_sig(A[i, j])
    normSq = 0
    for i in range(0, m):
        for j in range (0, n):
            normSq += pow(A[i, j], 2)
    norm = math.sqrt(normSq)
    return m*n, norm

m = 10
n = 5

print(frobenius(m, n))
