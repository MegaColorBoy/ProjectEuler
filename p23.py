# Project Euler: Problem 23 - Non-abundant numbers

#!usr/bin/python
import math, time, pe_lib

start = time.time()

limit = 28123
numbers = []
boolList = [False for i in range(limit)]

# generate a list of abundant numbers within the set limit
for i in range(1, limit):
	# if it's an abundant number, add to the list
	if pe_lib.isPerfectNumber(i) == 1:
		numbers.append(i)

# Now, generate a boolean list in which it stores the sum
# of two abundant numbers
for i in range(0, len(numbers)):
	for j in range(i, len(numbers)):
		temp = numbers[i] + numbers[j]
		# if it's within the limit, 
		# change it's appropriate boolean cell to True
		if temp < limit:
			boolList[temp] = True
		# Else, break out of the loop
		else:
			break

# Anything that's false, count it
count = 0
for i in range(0, len(boolList)):
	if boolList[i] == False:
		count += i

print count
print "Finished: %f seconds" % (time.time() - start)