import os
import sys
import copy
import collections

import nltk
import nltk.tokenize

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import pagerank

'''
    textrank.py
    -----------
    This module implements TextRank, an unsupervised keyword
    significance scoring algorithm. TextRank builds a weighted
    graph representation of a document using words as nodes
    and coocurrence frequencies between pairs of words as edge 
    weights. It then applies PageRank to this graph, and 
    treats the PageRank score of each word as its significance.
    The original research paper proposing this algorithm is
    available here:
    
        https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf
'''

## TextRank #####################################################################################
    
def preprocessDocument(document, relevantPosTags):
    '''
    This function accepts a string representation 
    of a document as input, and returns a tokenized
    list of words corresponding to that document.
    '''
    
    words = tokenizeWords(document)
    posTags = tagPartsOfSpeech(words)
    
    # Filter out words with irrelevant POS tags
    filteredWords = []
    for index, word in enumerate(words):
        word = word.lower()
        tag = posTags[index]
        if not isPunctuation(word) and tag in relevantPosTags:
            filteredWords.append(word)

    return filteredWords

def textrank(document, windowSize=2, randomSurferProb=0.15, relevantPosTags=["NN", "ADJ"]):
    '''
    This function accepts a string representation
    of a document and three hyperperameters as input.
    It returns Pandas matrix (that can be treated
    as a dictionary) that maps words in the
    document to their associated TextRank significance
    scores. Note that only words that are classified
    as having relevant POS tags are present in the
    map.
    '''
    
    # Tokenize document:
    words = preprocessDocument(document, relevantPosTags)
    
    # Build a weighted graph where nodes are words and
    # edge weights are the number of times words cooccur
    # within a window of predetermined size. In doing so
    # we double count each coocurrence, but that will not
    # alter relative weights which ultimately determine
    # TextRank scores.
    edgeWeights = collections.defaultdict(lambda: collections.Counter())
    for index, word in enumerate(words):
        for otherIndex in range(index - windowSize, index + windowSize + 1):
            if otherIndex >= 0 and otherIndex < len(words) and otherIndex != index:
                otherWord = words[otherIndex]
                edgeWeights[word][otherWord] += 1.0

    # Apply PageRank to the weighted graph:
    wordProbabilities = pagerank.powerIteration(edgeWeights, rsp=randomSurferProb)
    wordProbabilities.sort(ascending=False)

    return wordProbabilities

## NLP utilities ################################################################################

def asciiOnly(string):
    return "".join([char if ord(char) < 128 else "" for char in string])

PUNCTUATION = set([".", "?", "!", ",", "\"", ":", ";", "'", "-"])

def isPunctuation(word):
    return word in PUNCTUATION

def tagPartsOfSpeech(words):
    return [pair[1] for pair in nltk.pos_tag(words)]

def tokenizeWords(sentence):
    return nltk.tokenize.word_tokenize(sentence)

def tokenizeSentences(text):
    initial = nltk.tokenize.sent_tokenize(text)
    sentences = []
    for sentence in initial:
        sentences.append(sentence.replace("\n", " "))
    return sentences

## tests ########################################################################################

def applyTextRank(fileName, title):
    print
    print "Reading \"%s\" ..." % title
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    document = open(filePath).read()
    document = asciiOnly(document)
    
    print "Applying TextRank to \"%s\" ..." % title
    keywordScores = textrank(document)
    
    print
    header = "Keyword Significance Scores for \"%s\":" % title
    print header
    print "-" * len(header)
    print keywordScores
    print

def main():
    applyTextRank("Cinderalla.txt", "Cinderalla")
    applyTextRank("Beauty_and_the_Beast.txt", "Beauty and the Beast")
    applyTextRank("Rapunzel.txt", "Rapunzel")

if __name__ == "__main__":
    main()
