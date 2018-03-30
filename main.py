#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random 
import nltk 
from nltk.tokenize import word_tokenize

import parser

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
