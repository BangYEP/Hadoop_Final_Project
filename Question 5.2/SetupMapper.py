import sys

adjacency_list = []
current_node = None

pr = 1.0

for line in sys.stdin:

	if line[0] == '#' or line.strip() == "":
		continue

	n1, n2 = line.split('\t')
	n1 = n1.strip()
	n2 = n2.strip()

	if current_node == n1:
		adjacency_list.append(n2)

	else:
		if current_node != None:
			print (current_node, str(pr), ' '.join(adjacency_list))

		current_node = n1
		adjacency_list = [n2]

if current_node != None:
	print(current_node, str(pr), ' '.join(adjacency_list))


