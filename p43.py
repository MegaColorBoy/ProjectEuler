import time, math, pe_lib, itertools

start = time.time()
final = []
div = [1, 2, 3, 5, 7, 11, 13, 17]
pandigitals = pe_lib.genAllPandigitals()

for i in range(0, len(pandigitals)):
	arr = pe_lib.split_pandigital(pandigitals[i])
	count = 0
	for j in range(0, len(arr)):
		x = int(arr[j])
		# If it's divisible, count it
		if x % div[j] == 0:
			count += 1
		# else break the loop
		else:
			break
	
	# add the number to the list
	if count == 8:
		# print pandigitals[i]
		final.append(int(pandigitals[i]))

print "Sum of pandigital numbers with substring div property: %d " % sum(final)

print "Finished: %f seconds" % (time.time() - start)