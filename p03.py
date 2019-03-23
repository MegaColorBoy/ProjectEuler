# Project Euler: Problem 3 - Largest Prime Factor

#!usr/bin/python
import math
import time
import pe_lib

start = time.time()

x = 600851475143
list = pe_lib.primeFactors(x)

# Largest Prime Factor
print list[len(list)-1]

print "Finished in: %f" % (time.time() - start)