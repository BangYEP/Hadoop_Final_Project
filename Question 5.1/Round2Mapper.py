import sys

for line in sys.stdin:

	word, count = line.split('\t', 1)
	word, document = word.split(' ', 1)

	print(document,word + ' ' + count)
