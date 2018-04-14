# extract words from text and remove stopwords
import re

file = open("positive_words.txt",encoding='utf-8')
text = file.read().lower()
positive_words = re.sub('[,–]', '', text).split()

file = open("negative_words.txt",encoding='utf-8')
text = file.read().lower()
negative_words = re.sub('[,–]', '', text).split()

file = open("../news/news_1.txt",encoding='utf-8')
text = file.read().lower()




d = 256 # number of characters in input alphabet
q = 101 # q is a prime number
indexes = []
neutral = len(text)
def rabin_karp(text, pattern ,q):
	n = len(text)
	m = len(pattern)

	i = 0
	j = 0
	p = 0 # hash value of text
	t = 0 # hash value of pattern
	h = 1

	for i in range(m-1):
		h = (h*d)%q 

	for i in range(m):
		p = (d*p + ord(pattern[i])) % q # for pattern 
		t = (d*t + ord(text[i])) % q # for text of 1st box

	for i in range(n-m+1):
		if p==t:

			for j in range(m):
				if text[i+j] != pattern[j]:
					break
				j += 1
			if j == m:
				indexes.append(i)


		if i < n-m:
			t = (d*(t-ord(text[i])*h) + ord(text[i+m]))%q # text for next box

			if t < 0:
				t = t+q




for a in positive_words:
	rabin_karp(text, a, q)

	# if indexes != []:
	# 	print("pattern: " + a)
	# 	print(text[indexes[0]:indexes[0]+len(a)])
	# indexes = []
# print(len(indexes)) 
pos = len(indexes)

indexes = []
for a in negative_words:
	rabin_karp(text, a, q)
neg = len(indexes)

neutral -= (pos + neg)

# plot a word counts graph offline
import plotly
from plotly.graph_objs import *

plotly.offline.plot({
    "data": [Scatter(x=["Positive", "Negative", "Neutral"], y=[pos, neg, neutral])],
    "layout": Layout(title="+ve -ve words"),
})