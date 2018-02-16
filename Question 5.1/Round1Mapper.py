
import sys, os
import nltk
nltk.download('stopwords')

for line in sys.stdin:

	filename = os.path.basename(os.environ["mapreduce_map_input_file"])
    stopwords = nltk.corpus.stopwords.words('english')

	words = line.split(' ')
	for word in words:
		word = filter(str.isalpha, word).lower()

		if word == "" or word in stopwords:
			continue

		key = word + ' ' + filename;
		print (key, 1)
