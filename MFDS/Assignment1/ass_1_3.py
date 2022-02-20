import numpy as np
import math

def round_sig(x, d=5):
    if x == 0:
        return x
    # return round(x, d - math.floor(math.log10(abs(x))) - 1)
    return x

# Moved the back substitution process into its own subfunction for clarity
def back_substitution(A, b, n, n_op, n_swap=0):
    x = np.zeros(n)
    x[n-1] = round_sig(b[n-1] / A[n-1, n-1])
    n_op += 1
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = round_sig(sums - A[row,j] * x[j])
            n_op += 2
        x[row] = round_sig(sums / A[row,row])
        n_op += 1
    return x, n_op, n_swap

# Without pivoting
def gauss_elimination(A, b, n_op):
    n = A.shape[0]
    # Forward elimination
    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = round_sig(A[i,row] / A[row,row])
            n_op += 1
            for j in range(row, n):
                A[i,j] = round_sig(A[i,j] - factor * A[row,j])
                n_op += 2
            b[i] = round_sig(b[i] - factor * b[row])
            n_op += 2
    return back_substitution(A, b, n, n_op)

def gauss_elimination_pivoting(A, b, n_op, n_swap):
    n = A.shape[0]
    for row in range(0, n):
        for i in range(row+1, n):
            if np.abs(A[i, row]) > np.abs(A[row, row]):
                A[[row, i]] = A[[i, row]]
                temp = b[row]
                b[row] = b[i]
                b[i] = temp
                n_swap += 1
                break
        for i in range(row+1, n):
            factor = round_sig(A[i,row] / A[row,row])
            n_op += 1
            for j in range(row, n):
                A[i,j] = round_sig(A[i,j] - factor * A[row,j])
                n_op += 2
            b[i] = round_sig(b[i] - factor * b[row])
            n_op += 2
    return back_substitution(A, b, n, n_op, n_swap)

for n in range(1, 11):
    A = np.random.rand(n*100,n*100)
    b = np.random.rand(n*100)
    A = A*10
    b = b*10
    for i in range(0, n):
        b[i] = round_sig(b[i])
        for j in range(0, n):
            A[i, j] = round_sig(A[i, j])
    n_op_np = 0
    n_op_p = 0
    n_swap = 0
    X, n_op_np, n_swap = gauss_elimination(A, b, n_op_np)
    X, n_op_p, n_swap = gauss_elimination_pivoting(A, b, n_op_p, n_swap)
    m=float(n*100)

    max_op = (m*(m+1))/2 + (2*(2*m**3+3*m**2-5*m)/6) + 2*(m*(m+1)/2-m)


    print(n*100, n_op_p, n_op_np, max_op, n_swap)
