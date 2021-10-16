# PFDS Exercise 3
# Author: Anuroop Bisaria
# Given input string, check if palindrome

x = input("Enter a string: ")

if x == x[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
