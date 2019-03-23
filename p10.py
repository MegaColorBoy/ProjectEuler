import time
import pe_lib

start = time.time()
n = 2000000
print "Sum of 2 million primes: %d" % pe_lib.sumOfPrimesList(pe_lib.genPrimesTwo(n))
print "Finished in: %f" % (time.time() - start)