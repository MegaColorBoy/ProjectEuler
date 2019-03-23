import math, pe_lib, time

start = time.time()

circular = []

primes = pe_lib.genPrimesTwo(1000000)

for i in range(0, len(primes)):
	s = str(primes[i])
	count = 0

	# if it's single digit, add it anyways
	if len(s) == 1:
		circular.append(primes[i])

	elif len(s) > 1:
		count = 0
		# take a substring of length - 1 characters and
		# rotate it 
		for j in range(0, len(s)):
			s = s[1:len(s)] + s[:1]
			if pe_lib.checkPrime(int(s)):
				count += 1

		"""
		if it's a circular prime, 
		all of it's rotations must be prime and the count and the size of the 
		string must be the same (which indicates that it's a complete rotation)
		"""
		if count == len(s):
			circular.append(primes[i])

print "Number of circular primes found under 1 million: %d" % len(circular)
print "Finished in: %f" % (time.time() - start)