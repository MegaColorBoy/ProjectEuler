import time, math, pe_lib

# i = 7654321

# while pe_lib.isPrime_n_isPandigital(i) != True:
# 	i -= 1
# 	print i

# print "FINAL: %d" % i

primes = pe_lib.genPrimesTwo(7654321)

for i in range(len(primes), 0, -1):
	if pe_lib.checkPandigital(primes[i-1]):
		print primes[i-1]
		break