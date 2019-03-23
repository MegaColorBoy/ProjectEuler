import pe_lib, time

start = time.time()

coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200

print "Combinations for 200p: %d ways" % pe_lib.coinSum(coins, total)
print "Finished in: %f" % (time.time() - start)