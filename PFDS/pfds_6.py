# PFDS Exercise 6
# Author: Anuroop Bisaria
# Given n and r, calculate nCr

def fact(n):
    y = 1
    for i in range(2, n+1):
        y = y * i
    return y

def nCr(n, r):
    return (fact(n) / (fact(r) * fact(n - r)))

n = input("Enter n: ")
r = input("Enter r: ")
print(int(nCr(int(n), int(r))))
