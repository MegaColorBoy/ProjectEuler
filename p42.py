# Project Euler - Problem 42: Coded Triangle Numbers
import time, math, pe_lib

arr = []
word_str = ""

f = open("p042_words.txt", "r")
for line in f:
	word_str += line

arr = word_str.replace('"','').replace(',',' ').split(' ')

triangle_words = []

for i in range(0, len(arr)):
	x = pe_lib.words_to_numbers(arr[i])

	if(pe_lib.isTriangularNumber(x)):
		triangle_words.append(arr[i])

print len(triangle_words)