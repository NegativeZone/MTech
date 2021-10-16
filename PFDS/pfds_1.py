# PFDS Exercise 1
# Author: Anuroop Bisaria
# Given user input number, calculate the sum of its digits

x = input("Enter a number: ")
sum = 0
for digit in str(x):
    sum += int(digit)
print("Sum of digits: "+ str(sum))
