#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random 
import nltk 
from nltk.tokenize import word_tokenize

#to use NLTK, downloading an extra package is needed:
#(python) or (py3) -m nltk.downloader 'punkt'

def readDataLine(fname):

    linesRead = []
    	
    #file opening
    with open(fname, "r") as fp:

        for line in fp.readlines():
            if line.strip() == "": continue 	#skipping empty lines
            linesRead.append(line)	

    return linesRead


def modeOne(listModeOne, answerModeOne):

	loop = True

	while(loop):
		answerNum = random.randint(0,len(listModeOne)-1)
		answer = listModeOne[answerNum]
		if(answer != answerModeOne):
			loop = False

	printAnswer(answer)
 
	return answer


def printAnswer(answer):
	print("\tBot: " + answer)


def modeTwo():
	return


def contains(word):
	return

def createDict():
	return


def tokenizeSentence(sentence):

	sentWordList = word_tokenize(sentence)
	
	#affiche la liste des mots de la phrase
	#print("\nUeer said : ")
	#for s in sentWordList:
	#	print(s)

	return sentWordList


def tokenise_en(sent):

	sent = re.sub("([^ ])\'", r"\1 '", sent) # separate apostrophe from preceding word by a space if no space to left
	sent = re.sub(" \'", r" ' ", sent) # separate apostrophe from following word if a space if left

    # separate on punctuation
	cannot_precede = ["M", "Prof", "Sgt", "Lt", "Ltd", "co", "etc", "[A-Z]", "[Ii].e", "[eE].g"] # non-exhaustive list
	regex_cannot_precede = "(?:(?<!"+")(?<!".join(cannot_precede)+"))"
	sent = re.sub(regex_cannot_precede+"([\.\,\;\:\)\(\"\?\!]( |$))", r" \1", sent)
	sent = re.sub("((^| )[\.\?\!]) ([\.\?\!]( |$))", r"\1\2", sent) # then restick several fullstops ... or several ?? or !!
	sent = sent.split() # split on whitespace
	return sent


def botAnswer():
	return


if __name__=="__main__":	

	listModeOne = []
	listModeOne = readDataLine("./data/dataModeOne.txt")
	answerModeOne = ""

	while(True):
		inputUser = input("User: ")
		tokenizeSentence(inputUser)

		answerModeOne = modeOne(listModeOne, answerModeOne)
