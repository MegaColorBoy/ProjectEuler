# Project Euler: Problem 4 - Largest Palindromic Product

#!usr/bin/python
import math
import time
import pe_lib

start = time.time()

print pe_lib.largestPalindromeProduct(100, 999)

print "Finished in: %f" % (time.time() - start)