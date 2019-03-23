import math, pe_lib

def solutionsCount(p):
	count = 0

	for a in range(1,p+1):
		for b in range(a,p+1):
			c = p - a - b
			if b < c and ((a*a + b*b) == (c*c)):
				count += 1

	return count

maxCount = 0
maxLimit = 0

for p in range(1, 1001):
	print p
	count = solutionsCount(p)
	if maxCount < count:
		maxCount = count
		maxLimit = p

print maxCount, maxLimit
