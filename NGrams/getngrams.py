#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:22:08 2017

@author: khushalidave

Create script called getngrams.py. 

Your script should define the following functions:
processSentence(sentence,posLex,negLex,tagger):  The parameters of this function are a sentence (a string), a set positive words, a set of negative words, and a POS tagger.  The function should return a list with all the 4-grams in the sentence that have the following structure:                                                   

not <any word> <pos/neg word> <noun>. 

For example: not a good idea

 ---------------------------------------------------------------------------------------------
getTop3(D): The only parameter of this function is a dictionary D.  All the values in the dictionary are integers. The function returns a list of the keys with the 3 largest values in the dictionary.
"""
import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load
from operator import itemgetter
from nltk.corpus import stopwords

def removeDuplicates(line):
    lineWords=set()
    words=line.split(' ')
    
    for word in words:
        lineWords.add(word.strip())
        
    return lineWords

# return all the 'adv adj' twograms
def get4grams(sentence,posLex,negLex,tagger):
    result=[]
    sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
    sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

    #tokenize the sentence
    terms = nltk.word_tokenize(sentence.lower())
    POStags=['NN','NNS'] # POS tags of interest 		
    POSterms =getPOSterms(terms,POStags,tagger)
    
    singNouns=POSterms['NN']
    pluNouns=POSterms['NNS']
    
    fourgrams = ngrams(terms,4) #compute 2-grams    
   	 #for each 2gram
    for tg in fourgrams:  
        if tg[0] is 'not': 
             if tg[2] in posLex  or tg[2] in negLex:
                 if tg[3] in singNouns or tg[3] in pluNouns: # if the 4gram is a an adverb followed by an adjective
                      result.append(tg)

    return result

def getTop3(D):
    sortedByValue=sorted(D.items(),key=itemgetter(1),reverse=True)
    
    return sortedByValue[0:3] # return the top 3 terms and their frequencies 

# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms

def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname,encoding='utf-8')
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def run(fpath):

    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
     #load the positive and negative lexicons
    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')
    
    freq={} # keep the freq of each word in the file 

    stopLex=set(stopwords.words('english')) # build a set of english stopwrods 

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)
    print ('NUMBER OF SENTENCES: ',len(sentences))

    adjAfterAdv=[]

    # for each sentence
    for sentence in sentences:
        words=sentence.split(' ') # split to get the words in the sentence 
     
        adjAfterAdv+=get4grams(sentence,posLex,negLex,tagger)
        
        for word in words: # for each word in the sentence 
            if word=='' or word in stopLex:continue # ignore empty words and stopwords 
            else: freq[word]=freq.get(word,0)+1 # update the frequency of the word 
        D = getTop3(freq)
    return adjAfterAdv,D


if __name__=='__main__':
    print (run('input.txt'))




