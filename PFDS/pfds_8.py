# PFDS Exercise 8
# Author: Anuroop Bisaria
# Text file input and word count

file = open("textfile.txt", 'r')
x = file.read()
words = x.split()
spec = {i:words.count(i) for i in words}
sort_spec = sorted(spec, key=spec.get, reverse=True)

print('Number of words: ', len(words))
print('Top 3 words: ', sort_spec[0:3])
