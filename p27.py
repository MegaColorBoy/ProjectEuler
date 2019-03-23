# Project Euler: Problem 27 - Quadratic Primes
import math, pe_lib, time

start = time.time()

maxPrimeCount = 0
maxA = 0
maxB = 0

for a in range(-1000,1000):
	for b in range(-1000, 1000):
		n = 0
		while pe_lib.checkPrime(abs(n*n + a*n + b)):
			n += 1

		if n > maxPrimeCount:
			maxPrimeCount = n
			maxA = a
			maxB = b

print maxA, maxB, maxPrimeCount

print "Result: %d" %(maxA * maxB)
print "Finished in: %f" % (time.time() - start)