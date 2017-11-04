import copy


def contains_repeated(new_one):
	found = {}
	for node in new_one:
		if found.__contains__(node):
			return True
		else:
			found[node] = 1
	return False

edges = [(0,1),(1,2),(1,7),(2,3),(2,6),(3,4),(3,5),(4,5),(4,3),(5,6),(5,2),(6,7),(7,8),(7,9),(8,9)]

done = []

num_nodes = 9

print("STEP 1")
for e in edges:
	print(e)
print("\n")

for l in range(1,num_nodes-1):
	print("STEP {}".format(l+1))
	viable = []
	for edge1 in edges:
		for edge2 in edges:
			if edge1 != edge2 and edge1[-l:] == edge2[:l]:
				new_one = edge1+edge2[-1:]
				if edge1[0] == edge2[-1]:
					print(new_one+('*',))
					done.append(new_one+('*',))
				elif contains_repeated(new_one):
					print(new_one[-1:]+('!',))
					done.append(new_one[-1:]+('!',))
				elif new_one[-1] == num_nodes:
					print(new_one+('!',))
					done.append(new_one+('!',))
					# viable.append(new_one)
				else:
					print(new_one)
					viable.append(new_one)
	edges = copy.deepcopy(viable)
	print("\n")

print("RESULTS")
for i,d in enumerate(done):
	print("{}: {}".format(i, d))
