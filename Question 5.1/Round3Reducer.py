import sys, math

current_word = None
doc_count = 0
word = None
doc = None
words_per_doc = 0

counts = []

for line in sys.stdin:

	if line.strip() == "":
		continue

	word, val = line.split('\t', 1)
	doc, wordcount, words_per_doc = val.split(' ', 2)

	wordcount = int(wordcount)
	words_per_doc = int(words_per_doc)

	if current_word == word:
		counts.append((wordcount, words_per_doc, doc))
		doc_count += 1
	else:

		if current_word:
			for a, b, c in counts:
				tfidf = (float(a) / float(b)) * math.log(2.0 / float(doc_count))
				print (current_word, c, str(tfidf))

		counts = [(wordcount, words_per_doc, doc)]
		current_word = word
		doc_count = 1

if current_word == word:
	for a, b, c in counts:
		tfidf = (float(a) / float(b)) * math.log(2.0 / float(doc_count))
		print (current_word, c, str(tfidf))
	
