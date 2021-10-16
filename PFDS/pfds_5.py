# PFDS Exercise 5
# Author: Anuroop Bisaria
# Given input number, prime factorize

x = input("Enter a number: ")

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(int(x)))
