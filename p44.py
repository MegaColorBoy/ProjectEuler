# Project Euler - Problem 44: Pentagon Numbers
import time, math, pe_lib

found = False
i = 2
total = 0

while found != True:
	
	next_num = pe_lib.pentagonalNumber(i)

	for j in range(i-1, 0, -1):
		prev_num = pe_lib.pentagonalNumber(j)

		sum_pair = next_num + prev_num
		diff_pair = next_num - prev_num

		if pe_lib.isPentagonalNumber(sum_pair) and pe_lib.isPentagonalNumber(diff_pair):
			print next_num, prev_num
			total = diff_pair
			found = True
			break

	i += 1

print total