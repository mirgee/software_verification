str = \
"""
0000
0112
0221
1011
1120
1202
2022
2101
2210
"""

ret = ""

levels = [
	["CZ", "SK", "RU"],
	["muz", "zena", "muz"],
	["student", "produkcni", "duchodce"],
	["garsonka", "rodinny dům", "kolej"],
]

# Pro kazdou radku v ort. ctverci
for line in iter(str.splitlines()):
	# Pro kazdy charakter radku
	for i, char in enumerate(line):
		if i < len(levels):
			# Vypis prislusnou hodnotu faktoru
			ret += levels[i][int(char)]
			# Kvuli vypisu do LaTexu
			ret += " & " if i < len(levels) - 1 else " \\\\ "
	ret += "\n"

print(ret)
