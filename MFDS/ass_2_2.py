import itertools
import numpy as np
import math

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

def lower(a, x, y):
    k = np.zeros((x, y)).tolist()
    for i in range(0, x):
        for j in range(0, y):
            if i > j:
                k[i][j] = a[i][j]
    return k


def upper(a, x, y):
    k = np.zeros((x, y)).tolist()
    for i in range(0, x):
        for j in range(0, y):
            if i < j:
                k[i][j] = a[i][j]
    return k

def diagonal(a, x, y):
    k = np.zeros((x, y)).tolist()
    for i in range(0, x):
        k[i][i] = a[i][i]
    return k

def seidel(a, x ,b):
    n = len(a)
    for j in range(0, n):
        d = b[j]
        for i in range(0, n):
            if(j != i):
                d-=a[j][i] * x[i]
        x[j] = d / a[j][j]
    return x

for n in range(1, 10000):
    x = [0, 0, 0, 0]
    A = np.random.rand(4,4)
    A = A*10
    B = np.random.rand(1,4)
    B = B*10
    a = A.tolist()
    b = B[0].tolist()
    if isDiagDomSwapped(a) == True:
        print(a)
        print(b)
        D = diagonal(a, 4, 4)
        L = lower(a, 4, 4)
        U = upper(a, 4, 4)
        Dinv = np.linalg.inv(np.array(D)).tolist()
        LU = np.zeros((4, 4)).tolist()
        for i in range(4):
            for j in range(4):
                LU[i][j] = L[i][j] + U[i][j]
        iterMat = np.dot(Dinv, LU)
        print(iterMat)
        su=[sum(abs(i)) for i in iterMat]
        print (max(su))
        for i in range(4):
            su[i] = sum(row[i] for row in iterMat)
        print (max(su))
        frob = 0
        for i in range(4):
            for j in range(4):
                frob += iterMat[i][j]**2
        print(math.sqrt(frob))
        for i in range(0, 1000):
            x = seidel(a, x, b)
            print(x)
        break
    elif isDiagDomSwapped(a) == 'Swap':
        for k in list(itertools.permutations(A)):
            ans = isDiagDom(k)
            if  ans == True:
                print(k)
                print(b)
                D = diagonal(k, 4, 4)
                L = lower(k, 4, 4)
                U = upper(k, 4, 4)
                Dinv = np.linalg.inv(np.array(D)).tolist()
                LU = np.zeros((4, 4)).tolist()
                for i in range(4):
                    for j in range(4):
                        LU[i][j] = L[i][j] + U[i][j]
                iterMat = np.dot(Dinv, LU)
                print(iterMat)
                su=[sum(abs(i)) for i in iterMat]
                print ("Rowsum = ", max(su))
                for i in range(4):
                    su[i] = sum(row[i] for row in iterMat)
                print ("Colsum = ", max(su))
                frob = 0
                for i in range(4):
                    for j in range(4):
                        frob += iterMat[i][j]**2
                print("Frobenius = ", math.sqrt(frob))
                for i in range(0, 10):
                    x = seidel(k, x, b)
                    print(x)
                break
