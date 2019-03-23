# Project Euler: Problem 7 - 10001st Prime Number

#!usr/bin/python
import math
import time
import pe_lib

start = time.time()

count = 1
i = 2

while True:
	if pe_lib.isPrime(i):
		# When reaches this index, display the prime number and break
		if count == 10001:
			print i
			break
		else:
			count = count + 1
	i = i+1

print "Finished in: %f" % (time.time() - start)