import timeit
import numpy as np
import math
import matplotlib.pyplot as plt

t_add = 0
t_div = 0
t_mul = 0

sum = 0
start = timeit.default_timer()
for i in range(1, (10**6)+1):
    sum = sum+i
stop = timeit.default_timer()
t_add = (stop-start)/(10**6)

sum = 0
start = timeit.default_timer()
for i in range(1, (10**6)+1):
    sum = sum*i
stop = timeit.default_timer()
t_mul = (stop-start)/(10**6)

sum = 0
start = timeit.default_timer()
for i in range(1, (10**6)+1):
    sum = sum/i
stop = timeit.default_timer()
t_div = (stop-start)/(10**6)


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

x_res = []
y1_res = []
y2_res = []
y3_res = []
for n in range(1, 11):
    A = np.random.rand(n*100,n*100)
    b = np.random.rand(n*100)
    A = A*10
    b = b*10
    t_pivot = 0
    t_nopivot = 0
    for i in range(0, n):
        b[i] = round_sig(b[i])
        for j in range(0, n):
            A[i, j] = round_sig(A[i, j])
    start = timeit.default_timer()
    X = gauss_elimination(A, b)
    stop = timeit.default_timer()
    t_nopivot = stop - start
    start = timeit.default_timer()
    X = gauss_elimination_pivoting(A, b)
    stop = timeit.default_timer()
    t_pivot = stop - start
    m=float(n*100)
    t_theo = t_div*(m*(m+1))/2 + t_mul*(2*m**3+3*m**2-5*m)/6 + t_add*(2*m**3+3*m**2-5*m)/6 + t_add*(m*(m+1)/2-m) + t_mul*(m*(m+1)/2-m)
    print(n*100, t_theo, t_pivot, t_nopivot)
    x_res.append(n*100)
    y1_res.append(t_theo)
    y2_res.append(t_pivot)
    y3_res.append(t_nopivot)


# plt.plot(x_res, y1_res, color='r', label='theoretical')

plt.plot(x_res, y2_res, color='g', label='pivot')
plt.plot(np.unique(x_res), np.poly1d(np.polyfit(x_res, y2_res, 1))(np.unique(x_res)))
# plt.plot(x_res, y3_res, color='b', label='no pivot')
slope = np.polyfit(x_res, y2_res, 1)
print(slope[0])
plt.xlabel("Matrix Size")
plt.ylabel("Runtime")
plt.legend()
plt.show()
