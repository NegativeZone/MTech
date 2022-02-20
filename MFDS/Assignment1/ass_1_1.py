import timeit

sum = 0
start = timeit.default_timer()
for i in range(1, (10**6)+1):
    sum = sum/i
stop = timeit.default_timer()

print((stop-start)/(10**6))
