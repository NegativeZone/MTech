# PFDS Exercise 4
# Author: Anuroop Bisaria
# Given array with duplicate elements, print all elements and frequencies

x = ['a','a','b','a','b','b','c','d','a','d','e','e','a','f']

print({i:x.count(i) for i in x})
