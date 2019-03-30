import math, time, pe_lib, poker_lib

hands = ["5H 5C 6S 7S KD",
"2C 3S 8S 8D TD",
"5D 8C 9S JS AC",
"2C 5C 7D 8S QH",
"2D 9C AS AH AC",
"3D 6D 7D TD QD",
"4D 6S 9H QH QC",
"3D 6D 7H QD QS",
"2H 2D 4C 4D 4S",
"3C 3D 3S 9S 9D"]

for cards in hands:
	print poker_lib.determine_rank(cards)
