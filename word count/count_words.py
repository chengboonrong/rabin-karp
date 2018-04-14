# extract words from text and remove stopwords
import re
 
d = 256 # number of characters in input alphabet
q = 101 # q is a prime number
indexes= []
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

def stripNonAlphaNum(text):
	text = re.compile(r'\W+', re.UNICODE).split(text)
	number = ''.join(i for i in text if i.isdigit())
	return [w for w in text if w not in number]


def removeStopWords(wordlist, stopwords):
	return [w for w in wordlist if w not in stopwords]

def wordListToFreqDist(wordlist):
	wordfreq = [wordlist.count(p) for p in wordlist]
	return dict(zip(wordlist,wordfreq))

def sortFreqDict(wordfreq):
	temp = [(wordfreq[key],key) for key in wordfreq]
	temp.sort()
	temp.reverse()
	return temp

file = open("stopwords.txt",encoding='utf-8')
text = file.read().lower()
stopwords = text.split()


file = open("../news/news_2.txt",encoding='utf-8')
text = file.read().lower()

stopwords_from_text = []
for s in stopwords:
	rabin_karp(text, s, q)
	if indexes != []:
		# print("Pattern: " + s)
		# print(text[indexes[0]:indexes[0]+len(s)])
		stopwords_from_text.append(text[indexes[0]:indexes[0]+len(s)])
	indexes = []

full_Text = stripNonAlphaNum(text)
wordList = removeStopWords(full_Text, stopwords_from_text)
wordDict = wordListToFreqDist(wordList)
sortedDict = sortFreqDict(wordDict)
# for s in sortedDict: print (str(s))


# plot a word counts graph offline
import plotly
from plotly.graph_objs import *

plotly.offline.plot({
    "data": [Scatter(x=list(wordDict.keys()), y=list(wordDict.values()))],
    "layout": Layout(title="word count"),
})