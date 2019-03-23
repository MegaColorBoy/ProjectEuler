n = 1001
rings = (n-1)/2
total = 1
topR = total
for i in range(1,rings+1):
	topR += (8 * i)
	topL = topR - (2 * i)
	botL = topL - (2 * i)
	botR = botL - (2 * i)
	total += topR + topL + botL + botR

print total