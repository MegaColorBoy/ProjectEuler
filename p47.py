import time, math, pe_lib
save = 0
consec = 0
target = 4
arr = []

for i in range(0,200000):
	if pe_lib.num_of_prime_factors(i) == 4:
		save = i
		break

while consec < target:
	save += 1
	if pe_lib.num_of_prime_factors(save) == 4:
		consec += 1
		arr.append(save)
	else:
		consec = 0

print arr