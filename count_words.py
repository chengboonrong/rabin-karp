# extract words from text and remove stopwords
import re

def stripNonAlphaNum(text):
	return re.compile(r'\W+', re.UNICODE).split(text)

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

file = open("news/news_3.txt",encoding='utf-8')
text = file.read().lower()
full_Text = stripNonAlphaNum(text)
wordList = removeStopWords(full_Text, stopwords)
wordDict = wordListToFreqDist(wordList)
sortedDict = sortFreqDict(wordDict)
# for s in sortedDict: print (str(s))

# plot a word counts graph offline
import plotly
from plotly.graph_objs import *

plotly.tools.set_credentials_file(username='toshio97', api_key='weuJwHwO3oJkMOQmSrn3')
plotly.tools.set_config_file(plotly_domain='',
                             plotly_streaming_domain='',
                             world_readable=False
                             )

plotly.offline.plot({
    "data": [Scatter(x=list(wordDict.keys()), y=list(wordDict.values()))],
    "layout": Layout(title="word count"),
})