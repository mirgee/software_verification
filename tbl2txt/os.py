str = \
"""
0000000
1111110
2222220
0012120
1120200
2201010
0102211
1210021
2021101
0220111
1001221
2112001
0121022
1202102
2010212
0211202
1022012
2100122
"""

ret = ""

levels = [
	["Prum", "Sherlock", "SAPELI"],
	["YTONG", "Betong", "YTONG"],
	["50 cm", "60 cm", "70 cm"],
	["silikónová", "akrylátová", "silikónová"],
	["ano", "ne", "ano"]
]

for line in iter(str.splitlines()):
	for i, char in enumerate(line):
		if i < len(levels):
			ret += levels[i][int(char)]
			ret += " & " if i < len(levels) - 1 else " \\\\ "
	ret += "\n"

print(ret)
