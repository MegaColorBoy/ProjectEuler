# Project Euler: Problem 2 - Even Fibonacci Numbers

#!usr/bin/python
import math

max_sum = 0

Fib = [0,1]
EvenFib = []

for i in range(2,35):
	num = Fib[i-1] + Fib[i-2]

	if(num < 4000000):
		Fib.append(num)
		if(num % 2 == 0):
			EvenFib.append(num)
	else:
		print "Range: %d" % i
		break

print sum(EvenFib)