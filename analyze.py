import re
from collections import Counter 


def bigrams(text):
	return zip(text, text[1:])

def ngram(text, n):
	iterators = (text[gram:] for gram in range(1, n))
	grams = zip(text, *iterators)
	return grams

def get_counter(ngram):
	return Counter(ngram)

def prettify(outcome):
	return ''.join(l for l in outcome[0]), outcome[1]

with open('asimov.txt', 'r', encoding='utf-8') as file:
	text = file.read().lower()
	grams = ngram(text, 3)
	metrics = get_counter(grams)
	top_20 = metrics.most_common(100)
	for top in top_20:
		print(prettify(top))



