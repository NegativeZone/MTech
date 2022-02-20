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

def rowswap(A, r1, r2, c):
    for i in range(c):
        temp = A[r1, i]
        A[r1, i] = A[r2, i]
        A[r2, i] = temp
    return A

def matrix_rank(A):
    rank = len(A[0])
    for i in range(0, rank):
        if A[i, i] != 0:
            for j in range(0, len(A)):
                if j != i:
                    mul = A[j, i]/A[i, i]
                    for k in range(rank):
                        A[j, k] -= mul*A[i, k]
                else:
                    reduce = True
                    for k in range(i+1, len(A)):
                        if A[k, i] != 0:
                            rowswap(A, i, k, rank)
                            reduce = False
                            break
                    if reduce:
                        rank -= 1
                        for k in range(0, len(A)):
                            A[k, i] = A[k, rank]
                    i -= 1
    return rank

def gs_check(A):
    m = len(A)
    n = len(A[0])
    if m > n and matrix_rank(A) == min(m, n):
        print("Gram-Schmidt Applicable")
    else:
        print("Gram-Schmidt Not Applicable")

for i in range(0, 20):
    n = np.random.randint(1, 10)
    m = np.random.randint(n, 10)
    A = np.random.rand(m,n)
    for i in range(0, m):
        for j in range(0, n):
            while A[i, j] < 1:
                A[i, j] = A[i, j] * 10
            A[i, j] = round_sig(A[i, j])
    print(m, n)
    gs_check(A)
