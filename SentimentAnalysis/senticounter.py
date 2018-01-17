#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:38:05 2017

@author: khushalidave
"""
"""
Reads a list of reviews and return the count of positive words in reviews. 
"""

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname,encoding='utf-8')
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.lower().strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def removeDuplicates(line):
    lineWords=set()
    words=line.split(' ')
    
    for word in words:
        lineWords.add(word.strip())
        
    return lineWords
#function that reads in a file with reviews and decides if each review is positive or negative
#The function returns a list of the input reviews and a list of the respective decisions
def run(path):
    freq={} # new dictionary. Maps each word to each frequency 
    
    #load the positive and negative lexicons
    posLex=loadLexicon('positive-words.txt')
    
    fin=open(path)
    for line in fin: # for every line in the file (1 review per line)
        
        line=line.lower().strip()
        
        lineWords=removeDuplicates(line)
        
        for word in lineWords: #for every word in the review
            if word in posLex: # if the word is in the positive lexicon
                freq[word] = freq.get(word, 0) + 1
            
    fin.close()
    return freq


if __name__ == "__main__": 
    freq=run('textfile')
    for key in freq:
        print(key, freq[key])
       







