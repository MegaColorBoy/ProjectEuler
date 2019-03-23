list = []

for a in range(2, 101):
	for b in range(2, 101):
		x = a**b
		if x not in list:
			list.append(x)

print len(list)