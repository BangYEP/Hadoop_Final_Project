import sys

for line in sys.stdin:

	line = line.strip()

	# n = node
	# pr = pagerank
	# al = adjacency list
	n, val = line.split('\t', 1)
	pr, al = val.split(' ', 1)
	pr = float(pr)
	al = al.split(' ')

	# Printout the score for each node
	for out_node in al:
		print('%s\tscore %s' % (out_node, str(pr/float(len(al)))))

	# Also print the adjacency list
	print('%s\tnode %s' % (n, ' '.join(al)))