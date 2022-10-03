"""
Author: Chandana Thippeswamy
Date: 03-Oct-2022
Description: Implementation of a Multinomial Naive Bayes learning algorithm in Python for document classification
for datasets of IMDB movie reviews
File: W4_BayesianClassification.py
"""

import os

vocab = set()
posDict = {}
negDict = {}

def generateVocabulary(folderPath):

    listing = os.listdir(folderPath)
    # print('folderPath', folderPath)
    # Loop through all the files in the folder and collect the words of all files
    for file in listing:
        # open file for reading
        f = open(folderPath+'\\'+file, "r", encoding="utf8")

        # read file and split the contents
        allWords = f.read().split()

        # update the vocab set with unique words
        vocab.update(allWords)

        # close the file
        f.close()


def updateFrequency(folderPath, positiveDictionary, negativeDictionary):

    listing = os.listdir(folderPath)
    # print('folderPath', folderPath)
    # Loop through all the files in the folder and collect the words of all files
    for file in listing:
        # open file for reading
        f = open(folderPath+'\\'+file, "r", encoding="utf8")

        # read file and split the contents
        allWords = f.read().split()

        wordCount = len(allWords)


        # close the file
        f.close()


# Main call
if __name__ == '__main__':
    # Generate vocabulary list with words from positive review documents
    generateVocabulary('F:\MTU\PythonScripts\AILabs\MLLabs\imdb_data\data\\trainSmall\pos')

    # Update vocabulary list with words from negative review documents
    generateVocabulary('F:\MTU\PythonScripts\AILabs\MLLabs\imdb_data\data\\trainSmall\\neg')

    # Create dictionary for positive review words frequency with initial frequency as 0
    posDict = dict.fromkeys(vocab, 0)

    # Create dictionary for negative review words frequency with initial frequency as 0
    negDict = dict.fromkeys(vocab, 0)

