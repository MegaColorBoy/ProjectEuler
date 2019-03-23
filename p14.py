# Project Euler: Problem 14 - Largest Collatz Sequence

#!usr/bin/python
import math, time, pe_lib

start = time.time()

print pe_lib.largestCollatzSequence(1000000)

print "Finished: %f" % (time.time() - start)