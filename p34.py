import math, pe_lib

total = 0

for i in range(3, 100000):
	
	# convert to str
	s = str(i)

	fact = 0

	# if it's more than one 1 digit
	if len(s) > 1:
		for j in range(0, len(s)):
			fact += pe_lib.factorial(int(s[j]))

	# if it's a single digit
	else:
		fact = pe_lib.factorial(i)

	# if sum of factorial digits is equal to it's number
	if fact == i:
		total += i

print total