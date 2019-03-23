# Project Euler: Problem 16 - Power digit sum

#!usr/bin/python
import time, math, pe_lib

# 2 ^ 1000 -> converted to long -> converted to string
x = str(long(math.pow(2,1000)))

total = 0

# add all the digits
for i in range(0, len(x)):
	total += int(x[i])

print total