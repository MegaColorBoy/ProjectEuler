import math, time, pe_lib

pandigital = "123456789"

lowerBound = 9123
upperBound = 9876

arr = []

for i in range(lowerBound, upperBound+1):
	for j in range(1,3):
		pr = i * j

		s = str(i) + str(pr)
		sortedStr = ''.join(sorted(s))

		if sortedStr == pandigital:
			arr.append(s)

print sorted(arr)[len(arr)-1]