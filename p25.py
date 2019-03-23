# Project Euler: Problem 25 - 1000 digit Fibonacci Number
# this is a purely mathematical solution
import math, time

start = time.time()

limit = 999
golden_ratio = 1.6180

n = round(((limit * math.log(10)) + (math.log(5)/2))/(math.log(golden_ratio)))

print n
print "Finished in: %f" % (time.time() - start)