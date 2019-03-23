import math, time, pe_lib
limit = 1000000
start = time.time()
print pe_lib.consec_primes(limit)
print "Finished in: %f" % (time.time() - start)