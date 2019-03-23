numbers = []

for i in range(10, 1000000):
	x = list(str(i))
	y = 0
	for j in range(0, len(x)):
		y += int(x[j])**5
	
	if y == i:
		numbers.append(i)

print sum(numbers)
