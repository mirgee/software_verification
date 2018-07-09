# -*- coding: utf8 -*-
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

levels = [
	["CZ", "UK", "RU"],
	["muz", "zena"],
	["student", "produkcni", "duchodce"],
	["garsonka", "rodinny dum", "kolej"]
]

pairwise = all_pairs( levels )

for i, v in enumerate(pairwise):
	print "%i:\t%s" % (i, str(v))