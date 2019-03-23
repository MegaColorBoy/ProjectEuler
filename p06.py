# Project Euler: Problem 6 - Sum Square Difference

#!usr/bin/python
import math
import time
import pe_lib

start = time.time()

print pe_lib.squareOfSum(100) - pe_lib.sumOfSquares(100)

print "Finished in: %f" % (time.time() - start)