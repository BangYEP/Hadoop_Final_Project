import sys

current_node = None
lines = []

# Damping factor
d = 0.85

# Takes a list of lines for the same node, with the last line being different
def process_node(ls):

	# pr = pagerank, al = adjacency list, n = node
	pr = 0
	al = []
	node = None
	for l in ls:

		# n = node, val = value
		n, val = l.split('\t', 1)

		# t = type
		t, val = val.split(' ', 1)

		# Node line
		if t == 'node':
			al = val
			node = n
		# Score line
		elif t == 'score':
			pr += float(val)
		# Shouldn't happen...
		else:
			raise Exception('Unknown type found')

	pr = (1.0 - d) + (d * pr)

	# If node is none it means we didn't find an adjacencylist for this node
	if node == None:
		pass
	else:
		print('%s\t%s %s' % (node, str(pr), al))


for line in sys.stdin:

	line = line.strip()
	node = line.split('\t', 1)[0][:-1] # Skip the last char which is used for a sorting trick

	# If this is the first node, set the current node
	if current_node == None:
		current_node = node

	# Process this node if we have all the information for it
	if current_node != node:

		# Process the node
		process_node(lines)

		# Update to the new current node
		current_node = node
		lines = [line]

	# Otherwise, append the line and continue
	else:
		lines.append(line)

if current_node != None:
	process_node(lines)




