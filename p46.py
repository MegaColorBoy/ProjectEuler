import time, math, pe_lib

primes = pe_lib.genPrimesTwo(10000)
res = 1
notFound = True

while notFound:
	
	res += 2 # every odd number
	count = 0
	notFound = False

	while res >= primes[count]:
		if pe_lib.isDoubleSquare(res - primes[count]):
			notFound = True
			break
		count += 1

print res