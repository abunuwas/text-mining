import re
from collections import Counter 
import itertools 

def bigrams(text):
	return zip(text, text[1:])

def ngram_seq(sequence, n):
	iterators = (sequence[gram:] for gram in range(1, n))
	grams = zip(sequence, *iterators)
	return grams

def ngram_iter(iterable, n):
	backward, forward = itertools.tee(iterable)
	next(forward)
	return zip(backward, forward)

def get_counter(ngram):
	return Counter(ngram)

def prettify(outcome):
	return ''.join(l for l in outcome[0]), outcome[1]

#text = 'hola me llamo jose y esta es mi casa en la que vivo tranquilamente, y me encanta!'

def words(text, pos):
	regex = re.compile(r"\w+")
	return regex.finditer(text, pos)

#for word1, word2 in ngram_iter(words(text, 0), 2):
#	print(word1.group(), word2.group())

#for i, e in zip(backward, backward):
#	print(i.group(), e.group())

with open('asimov.txt', 'r', encoding='utf-8') as file:
	text = file.read().lower()
	grams = ngram_iter(words(text, 0), 2)
	metrics = get_counter(grams)
	top_20 = metrics.most_common(100)
	for top1, top2 in top_20:
		word1, word2 = top1
		metric2 = top2
		print(word1.group(), word2.group(), metric2)
		#print(prettify(top))



