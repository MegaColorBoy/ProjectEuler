import time, math, pe_lib

total = 0
for i in range(1, 1001):
	total += i ** i

s = str(total)

print s[-10:]