# Project Euler: Problem 36 - Double-base palindromes
import math, time, pe_lib

start = time.time()

arr = []

for i in range(1,1000000):
	if pe_lib.checkPalindrome(i):
		binary = pe_lib.base10tobase2(i)

		if binary == binary[::-1]:
			arr.append(i)

print sum(arr)
print "Finished in: %f" % (time.time() - start)
