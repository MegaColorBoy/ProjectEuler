# Project Euler: Problem 1 - Multiples of 3 and 5

#!usr/bin/python

total_sum = 0

for num in range(1,1000):
	if(num % 3 == 0 or num % 5 == 0):
		total_sum += num

print "Total: %s" % total_sum