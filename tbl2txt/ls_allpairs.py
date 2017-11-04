# -*- coding: utf8 -*-
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

levels = [
	["CZ", "UK", "US"],
	["muz", "zena"],
	["student/ka", "technik", "duchodce/kyne"],
	["svobodbny/a", "rozvedeny/a"],
	["venkov", "mesto"],
	["garsonka", "chata", "kolej"]
]

pairwise = all_pairs( levels )

for i, v in enumerate(pairwise):
	print "%i:\t%s" % (i, str(v))