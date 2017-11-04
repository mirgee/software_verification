import copy


def contains_repeated(new_one):
	found = {}
	for node in new_one:
		if found.__contains__(node):
			return True
		else:
			found[node] = 1
	return False


def is_circular(arr1, arr2):
	if len(arr1) != len(arr2):
		return False

	str1 = ' '.join(map(str, arr1[:-1]))
	str2 = ' '.join(map(str, arr2[:-1]))
	if len(str1) != len(str2):
		return False

	return str1 in str2 + ' ' + str2

edges = [(0,1),(1,2),(1,7),(2,3),(2,6),(3,4),(3,5),(4,3),(5,2),(6,7),(7,8)]

done = []
prev_exclams = [(7,9),(8,9)]
next_exclams = []

num_nodes = 9

print("STEP 1")
for e in edges+prev_exclams:
	print(e)
print("\n")

for l in range(1,num_nodes-1):
	print("STEP {}".format(l+1))
	viable = []
	for x in prev_exclams:
		edges.append(x)
	# Vykricniky, ktere se v danem kroku nepodari rozsirit, jsou hotove
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
					if edge1 in prev_exclams:
						prev_exclams.remove(edge1)
					elif edge2 in prev_exclams:
						prev_exclams.remove(edge2)
					next_exclams.append(new_one)
				else:
					print(new_one)
					viable.append(new_one)
	for x in prev_exclams:
		done.append(x+("!",))
	# print("NEXT EXCLAMS")
	# for x in next_exclams:
	# 	print(x)
	prev_exclams = copy.deepcopy(next_exclams)
	next_exclams.clear()
	edges = copy.deepcopy(viable)
	print("\n")

for d1 in done:
	if d1[-1] == "*":
		for d2 in done:
			if d1 != d2 and is_circular(d1[:-1],d2[:-1]):
				done.remove(d2)

print("RESULTS")
for i,d in enumerate(done):
	print("{}: {}".format(i, d))

print("\nFOR LATEX")
for i,d in enumerate(done):
	print("\item {} $\\rightarrow$ {}".format(i, ','.join(map(str,d[:-1]))))