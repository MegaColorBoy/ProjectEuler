import math, time, pe_lib

def prime_perm(n):
	arr = []
	s = str(n)
	for i in range(0, len(s)-1):
		s = s[1:3] + s[0] + s[len(s)-1]
		if pe_lib.checkPrime(int(s)):
			x = int(s)
			if pe_lib.num_digits(x) == 4:
				arr.append(int(s))
	return arr

primes = pe_lib.genPrimesTwo(9999)

for i in range(0,len(primes)):
	x = primes[i]
	
	perms = prime_perm(x)
	perms.sort()

	if len(perms) == 3:
		count = 0

		for j in range(0, len(perms)-1):
			if perms[j+1] - perms[j] == 3330:
				count += 1

		if perms[len(perms)-1] - 6660 == perms[0]:
			count += 1

		if count == 3:
			print perms