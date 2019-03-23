import math, pe_lib
np = 1
dp = 1

for c in range(1,10):
	for d in range(1, c):
		for n in range(1, d):

			num_pr = (10 * n + c) * d
			den_pr = (10 * c + d) * n

			if num_pr == den_pr:
				np *= n
				dp *= d

final = dp / pe_lib.gcd(np,dp)
print final