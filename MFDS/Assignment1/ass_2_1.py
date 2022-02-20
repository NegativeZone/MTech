import itertools
import numpy as np

def isDiagDom(A):
    n = len(A)
    for i in range(0, n) :
        sum = 0
        for j in range(0, n) :
            sum = sum + abs(A[i][j])
        sum = sum - abs(A[i][i])
        if (abs(A[i][i]) < sum) :
            return False
    return True

def isDiagDomSwapped(A):
    if isDiagDom(A) == True:
        return True
    else:
        ans = 0
        for k in list(itertools.permutations(A)):
            ans = isDiagDom(k)
            if  ans == True:
                return "Swap"
        return False


# A = [[ 3, -2, 7 ],
#     [ -1, 6, 4 ],
#     [ 7, -1, 2 ]]
#
# print(isDiagDomSwapped(A))

for n in range(1, 100):
    A = np.random.rand(3,3)
    A = A*10
    if isDiagDomSwapped(A.tolist()) == True:
        print(A.tolist())
