
squares = [[(0, 2, 4, 1, 3), (4, 1, 3, 0, 2), (3, 0, 2, 4, 1), (2, 4, 1, 3, 0), (1, 3, 0, 2, 4)],
[(0, 3, 1, 4, 2), (3, 1, 4, 2, 0), (1, 4, 2, 0, 3), (4, 2, 0, 3, 1), (2, 0, 3, 1, 4)],
[(0, 4, 3, 2, 1), (2, 1, 0, 4, 3), (4, 3, 2, 1, 0), (1, 0, 4, 3, 2), (3, 2, 1, 0, 4)],
[(0, 1, 2, 3, 4), (4, 0, 1, 2, 3), (3, 4, 0, 1, 2), (2, 3, 4, 0, 1), (1, 2, 3, 4, 0)]]

levels = [
	["CZ", "UK", "US", "CZ", "UK"],
	["muž", "žena", "muž", "žena", "muž"],
	["student/ka", "technik", "důchodce/kyně", "student/ka", "technik"],
	["svobodbný/á", "rozvedený/á", "svobodný/á", "rozvedený/á", "svobodbný/á"],
	["venkov", "město", "venkov", "město", "venkov"],
	["garsonka", "chata", "kolej", "garsonka", "chata"]
]

ret = ""

for row in range(len(levels)-1):
	for col in range(len(levels)-1):
		ret += levels[0][row] + " & "
		ret += levels[1][col] + " & "
		for i, square in enumerate(squares[:len(levels)-2]):
			ret += levels[i+2][square[row][col]]
			ret += " & " if i < len(levels) - 3 else " \\\\ \n"

print(ret)
