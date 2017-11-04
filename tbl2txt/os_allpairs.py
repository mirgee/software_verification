import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

levels = [
	["Prum", "Sherlock", "SAPELI"],
	["YTONG", "Betong"],
	["50 cm", "60 cm", "70 cm"],
	["silikonova", "akrylatova"],
	["ano", "ne"]
]

pairwise = all_pairs( levels )

for i, v in enumerate(pairwise):
	print "%i:\t%s" % (i, str(v))