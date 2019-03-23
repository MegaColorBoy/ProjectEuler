import math, time, pe_lib

start = time.time()

primes = pe_lib.genPrimesTwo(1000000)
primesSet = set(primes)
arr = []

for i in range(0, len(primes)):
	n = primes[i]
	digits = len(str(n))

	# truncate from left to right
	ltr_arr = pe_lib.ltr_truncate(n)

	# truncate from right to left
	rtl_arr = pe_lib.rtl_truncate(n)

	ltr_set = set(ltr_arr) & primesSet
	rtl_set = set(rtl_arr) & primesSet

	if n > 7:
		if len(ltr_set) == digits and len(rtl_set) == digits:
			arr.append(n)

print "The sum of 11 truncatable primes: %d" % sum(arr)
print "Finished in: %f" % (time.time() - start)