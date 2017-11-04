import networkx as nx

edges = [(1,2),(2,3),(3,4),(3,5),(4,5),(5,6),(5,12),(6,7),(6,8),(7,6),(8,9),(8,10),(9,8),
         (10,11),(11,5)]
defs = [1,2,11]
uses = [7,10,12]

g = nx.DiGraph()
# g = nx.random_regular_graph(2, 5)
g.add_edges_from(edges)

res = ""

for source in g.nodes():
	for target in g.nodes():
		candidates = nx.all_simple_paths(g, source=source, target=target)
		candidates = list(filter(lambda path: not any(d in path for d in defs), candidates))
		res += "du({},{},a999) = {}\n".format(source, target, candidates) if len(candidates) > 0 else ""

print(res)