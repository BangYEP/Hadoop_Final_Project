import sys

current_doc = None
current_count = 0
word_count = {}
doc = None


lines = []

for line in sys.stdin:

	if line.strip() == "":
		continue

	lines.append(line)

	doc, val = line.split('\t', 1)
	word, count = val.split(' ', 1)
	count = int(count)

	if current_doc == doc:
		current_count += count

	else:
		if current_doc:
			word_count[current_doc] = current_count
		current_count = count
		current_doc = doc

if current_doc == doc:
	word_count[current_doc] = current_count


for line in lines:
	doc, val = line.split('\t', 1)
	word, count = val.split(' ', 1)
	print(word, doc, count.strip(), str(word_count[doc]))



