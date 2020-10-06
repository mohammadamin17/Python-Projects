"""A simple Sentiment Analyzer that uses a lexicon, which is a dataset of words and their corresponding sentiment.
for example, Sad = negative sentiment, Happy = positive sentiment.

The program reads an input sentence from the user and calculates the total sentiment of that sentence (with a positive 1 or negative 1 score for each word in the lexicon).
If the word does not exist in the lexicon, the analyzer just skips it.
Here is an example.
If the user enters something like:
The movie has amazing plot but bad ending but I still like it.

The lexicon is going to match ("amazing", "bad", and "like") and the sentiments would be (+1, -1, +1) respectively, so the overall sentiment is the sum of scores divided by the number of sentiments"""

user_input = input("Please type in your sentence: ")

d={}

with open("negative_words.txt") as neg:
    for word in neg:
        d[word.strip()] = -1

with open("positive_words.txt") as pos:
    for word in pos:
        d[word.strip()] = 1

def calculate_sentiment(sentence):
    sentence_score=0
    normalizer = 0
    for w in sentence.split(" "):
        if w in d:
            sentence_score += d[w]
            normalizer += 1
    return sentence_score/normalizer

print(calculate_sentiment(user_input))
