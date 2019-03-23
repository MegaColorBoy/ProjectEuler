# Project Euler: Problem 40 - Champernowne's Constant

import time, math, pe_lib

i = 1
digits = '1'
product = 1
fractionals = [1, 10, 100, 1000, 10000, 100000, 1000000]

while len(digits) <= 1000000:
	i += 1
	digits += str(i)

for i in range(0, len(fractionals)):
	# print digits[fractionals[i]-1]
	product *= int(digits[fractionals[i]-1])

print product
