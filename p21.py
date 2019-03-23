# Project Euler: Problem 21 - Amicable Numbers

#!usr/bin/python
import math, time, pe_lib
start = time.time()
print pe_lib.amicableNumbers(10000)
print "Finished: %f seconds" % (time.time() - start)