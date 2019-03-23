# Project Euler: Problem 18 and 67 - Maximum Path Sum I and II

#!usr/bin/python
import time, math, pe_lib

num_str = ""

# read text file
f = open("triangle2.txt", "r")
for line in f:
	num_str += line
f.close()

# convert the string numbers to integers in the list
list = map(int, num_str.replace('\n', ' ').split(' '));

start = time.time()
print pe_lib.maxPathSum(list)
print "Finished: %f seconds" % (time.time() - start)