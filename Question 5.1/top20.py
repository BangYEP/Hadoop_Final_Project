import sys

words = []

for line in sys.stdin:

	key, tfidf = line.split('\t', 1)
	word, doc = key.split(' ', 1)

	words.append((word, tfidf.strip()))

res = sorted(words, key=lambda x: x[1], reverse=True)[:20]

for w, v in res:
	print(w, v)