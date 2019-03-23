import time, math, pe_lib

# start from 144 as 143 has been solved in the problem statement
i = 144
found = False

while found != True:

	triangularNumber = pe_lib.triangleNumber(i)
	pentagonalNumber = pe_lib.pentagonalNumber(i)
	hexagonalNumber = pe_lib.hexagonalNumber(i)

	isPentagonal = pe_lib.isPentagonalNumber(hexagonalNumber)
	isTriangular = pe_lib.isTriangularNumber(hexagonalNumber)

	if isPentagonal and isTriangular:
		print triangularNumber, pentagonalNumber, hexagonalNumber
		found = True
		break

	i += 1