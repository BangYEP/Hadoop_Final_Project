import sys

for line in sys.stdin:

	key, val = line.split('\t', 1)
	word, doc = key.split(' ', 1)
	word_count, words_per_doc = val.split(' ', 1)

	print (word, doc, word_count, words_per_doc)
