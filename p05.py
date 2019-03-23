# Project Euler: Problem 5 - Smallest Multiple

#!usr/bin/python
import math
import time
import pe_lib

start = time.time()

print pe_lib.smallestMultiple(20)	

# equivalent version of it
# print reduce(pe_lib.lcm, range(1,20)

print "Finished in: %f" % (time.time() - start)