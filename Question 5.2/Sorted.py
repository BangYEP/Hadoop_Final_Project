import sys

data = []
for line in sys.stdin:

	line = line.strip()
	node, val = line.split('\t',1)
	pr = float(val.split(' ',1)[0])
	data.append((node, pr))

for a in sorted(data, key=lambda x: x[1], reverse=True)[:20]:
	print(a)
