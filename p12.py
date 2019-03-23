# Project Euler: Problem 12 - Highly Divisible Triangular Number

#!usr/bin/python
import math, time, pe_lib

start = time.time()

num = 0
i = 1

while pe_lib.trialDivision(num) < 500:
	num += i
	i += 1

print num
print "Finished: %f" % (time.time() - start)