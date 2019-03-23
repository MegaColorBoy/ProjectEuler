# Project Euler: Problem 26 - Reciprocal Cycles
# Solved using a simple math solution
import math, pe_lib

start = time.time()

max_index = 0
max_length = 0

for i in range(2, 990):
	if pe_lib.isPrime(i) == 1:
		x = str(pe_lib.repeatingDecimals(i))

		if len(x) > max_length:
			max_length = len(x)
			max_index = i

print max_index
print "Finished in: %f" % (time.time() - start)