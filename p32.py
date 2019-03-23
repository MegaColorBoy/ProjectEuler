import math

pandigital = "123456789"
arr = []

for i in range(1, 10000):
	for j in range(1,10000):

		pr = i * j
		pr_str = (str(i) + str(j) + str(pr))
		pr_str = ''.join(sorted(pr_str))

		if len(pandigital) == len(pr_str):
			if pandigital == pr_str:
				if pr not in arr:
					arr.append(pr)
					print i, j, pr