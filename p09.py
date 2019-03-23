# Project Euler: Problem 9 - Special Pythagorean Triplet

#!usr/bin/python

import time
import math
import pe_lib

start = time.time()

sum = 1000

for a in range(1,500):
	for b in range(a+1, 500):
	
		# a + b + c = sum
		# so, c = sum - a - b
		c = sum - a - b

		a2 = a*a
		b2 = b*b
		c2 = c*c

		if (a2+b2 == c2) and (a+b+c == sum):
			print "Triplet: [%d, %d, %d]" % (a,b,c)

print "Finished in: %f seconds" % (time.time() - start)
