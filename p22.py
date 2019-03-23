# Project Euler: Problem 22 - Names Scores

#!usr/bin/python
import math, time, pe_lib
start = time.time()

word_str = "";
refStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
totalScore = 0;

# read text file
f = open("names.txt", "r")
for line in f:
	word_str += line
f.close()

list = word_str.replace('"', '').replace(",",' ').split(' ');
list.sort()

for i in range(len(list)):
	name = list[i]
	count = 0
	for j in range(len(name)):
		count += (refStr.find(name[j])) + 1

	count *= (i + 1)
	totalScore += count

print "Total name scores: %d" % (totalScore)

print "Finished: %f seconds" % (time.time() - start)