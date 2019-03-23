# Project Euler: Problem 24 - Lexicographical Permutation
#!usr/bin/python
import math, time, pe_lib

start = time.time()

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 1
limit = 1000000

while count < limit:
	pe_lib.nextPermutation(list)
	count = count + 1

print "".join(str(x) for x in list)
print "Finished: %f seconds" % (time.time() - start)
