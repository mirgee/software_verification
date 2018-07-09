import networkx as nx

edges = [(1,2),(2,3),(3,4),(2,4),(4,5),(5,6),(5,10),(6,7),(6,8),(7,6),(8,9),(9,5)]
defs = [1,8]
uses = [7,10]

g = nx.DiGraph()
# g = nx.random_regular_graph(2, 5)
g.add_edges_from(edges)

res = ""

# Zacatek
for source in g.nodes():
	# Konec
	for target in g.nodes():
		# Pokud je zacatek mezi hledanymi defy a konec mezi use
		if (source in defs) and (target in uses):
			# Najdi jednoduche cesty
			candidates = nx.all_simple_paths(g, source=source, target=target)
			# Musi byt def-ciste
			candidates = list(filter(lambda path: not any(d in path[1:] for d in defs), candidates))
			# Vypis
			res += "du({},{},a999) = {}\n".format(source, target, candidates) if len(candidates) > 0 else ""

print(res)