### WIA2005 Group Project | Topic 2: String Matching for sentiment analysis

1. Identify and use 5-10 webpages such as BBC New, Bernama, Al Jazeera and others on topics regarding political/education/economic news in Malaysia.

2. Extract the webpages text and count the number of words in the webpages.
  + Sometimes a webpage must be converted to the text version before it can be done
    i. Guide 1: You may refer to [this website](https://www.textise.net) to extract word from a website 
  +. Guide 2: You may refer to [this website](https://programminghistorian.org/lessons/counting-frequencies) on how to count word frequency in a website
  +. You can also filter stops words from the text you found
    i. Guide 3: Stops words are such as conjunctions and prepositions. You may refer to [this link](https://www.ranks.nl/stopwords)
    ii. Program using Rabin-karp algorithm to find and delete the stop words.

3. Plot line/scatter/histogram graphs related to the word count using Plotly (Word count, stop words)
  + Guide 4: You may refer this link on how to install [Plotly](https://plot.ly/python/getting-started/) and how to use the API keys

4. Compare words in the webpages with the positive, negative and neutral English words using **_Rabin-Karp String Matching algorithm_**
  + Guide 5: Use the following word as [positive](http://positivewordsresearch.com/list-of-positive-words/) and [negative](http://positivewordsresearch.com/list-of-negative-words/) English words  
    i. Put these words in a text file for you to access them in your algorithm
    ii. Words that are not in the list can be considered as neutral
    
5. Plot histogram graphs of positive and negative words found in the webpages.
  + Guide 6: Use Plotly
  
6. Give an algorithmic conclusion regarding the sentiment of those articles
  + Guide 7: If there are more positive words, conclude that the article is giving positive sentiment, if there are more negative words, conclude that the article is giving negative sentiment.
  i. You may try to conclude in different perspectives such as whether the list of positive and negative words above is accurate to be used in the context of the article you extracted the text.
