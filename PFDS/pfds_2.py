# PFDS Exercise 2
# Author: Anuroop Bisaria
# Given a number and order, check for Armstrong number

x = input("Enter a number: ")
y = input("Enter Armstrong order: ")

sum = 0
for digit in str(x):
    sum += int(digit) ** int(y)

if sum == int(x):
    print(x, "is an Armstrong number of order", y)
else:
    print(x, "is not an Armstrong number of order", y)
