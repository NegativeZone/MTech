import numpy as np
import math

# Rounding function for significant figures
def round_sig(x, d=5):
    if x == 0:
        return x
    return round(x, d - math.floor(math.log10(abs(x))) - 1)

# Moved the back substitution process into its own subfunction for clarity
def back_substitution(A, b, n):
    x = np.zeros(n)
    x[n-1] = round_sig(b[n-1] / A[n-1, n-1])
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = round_sig(sums - A[row,j] * x[j])
        x[row] = round_sig(sums / A[row,row])
    return x

# Without pivoting
def gauss_elimination(A, b):
    n = A.shape[0]
    # Check if pivot needed
    if any(np.diag(A)==0):
        raise ZeroDivisionError(("Can't divide by 0"))
    # Forward elimination
    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = round_sig(A[i,row] / A[row,row])
            for j in range(row, n):
                A[i,j] = round_sig(A[i,j] - factor * A[row,j])
            b[i] = round_sig(b[i] - factor * b[row])
    return back_substitution(A, b, n)

def gauss_elimination_pivoting(A, b):
    n = A.shape[0]
    # Check for pivots
    for row in range(0, n):
        for i in range(row+1, n):
            if np.abs(A[i, row]) > np.abs(A[row, row]):
                A[[row, i]] = A[[i, row]]
                b[row], b[i] = b[i], b[row]
                break
        for i in range(row+1, n):
            factor = round_sig(A[i,row] / A[row,row])
            for j in range(row, n):
                A[i,j] = round_sig(A[i,j] - factor * A[row,j])
            b[i] = round_sig(b[i] - factor * b[row])
    return back_substitution(A, b, n)

A = np.array([[2,4],[3,9]])
b = np.array([2,30])
# A = np.array([[8,-2,-1,0,0],[-2,9,-4,-1,0],[-1,-3,7,-1,2],[0,-4,-2,12,-5],[0,0,-7,-3,15]])
# b = np.array([5,2,0,1,5])

print(gauss_elimination_pivoting(A, b))
print(gauss_elimination(A, b))
