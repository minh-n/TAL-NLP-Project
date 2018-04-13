#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import re
import os
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


def modeOne(listModeOne, answerModeOne, appendString):

	loop = True

	while(loop):
		answerNum = random.randint(0,len(listModeOne)-1)
		answer = listModeOne[answerNum]
		if(answer != answerModeOne):
			loop = False
		if(appendString != None):
			mystring = answer
			pattern = re.compile(r'<.+>')
			newstring = pattern.sub(appendString, mystring)
			answer = newstring
 	
	return answer

def answerVerb(sentString, verb):

	ans = ""
	buff = sentString[sentString.index(verb) + len(verb):]

	if verb == "was":
		ans = "Why were you" + buff + "?"

	elif verb == "am":
		ans = "Why are you" + buff + "?"

	return ans


def printAnswer(answer):
	print("\tBot: " + answer)


def modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo):
    tag = None
    answer = ""
    
    currentWord = ""

    #for cle, value in dictModeTwo.items():
        #print("mot : {}, tag : {}".format(cle, value))
    for word in sent:
        #print(word)
        if word in dictVerb:
        	sentString = ' '.join(sent)
        	answer = answerVerb(sentString, word)
        	break
        if word in dictModeTwo:
            currentWord = word 			#an useful word is memorized
            tag = dictModeTwo[word]
            break


    if tag != None:						#computing the answer depending on its tag
        if tag == "tagAI.txt":
            answer = modeOne(answerAI, answerModeTwo, None)
        elif tag == "tagCharacter.txt":
            answer = modeOne(answerCharacter, answerModeTwo, currentWord)
        elif tag == "tagInventory.txt":
            answer = modeOne(answerInventory, answerModeTwo, currentWord)
        elif tag == "tagEnvironment.txt":
            answer = modeOne(answerEnvironment, answerModeTwo, currentWord)
        elif tag == "tagInfo.txt":
            answer = modeOne(answerInfo, answerModeTwo)
        else:
            print("DEBUG : tagging error (this line should not appear)!")
    return answer

def contains(word):
	return

def createDict():
    dict = {}
    for element in os.listdir("../data/dataModeTwo"):
        with open("../data/dataModeTwo/" + element, "r") as fp:
            for line in fp.readlines():
                if line.strip() == "": continue 		#skipping empty lines
                linelen = len(line)-1               	#removing \n 
                line = line[:linelen]
                dict[line] = element    
    return dict

def createDictVerb():
    dict = {}
    with open("../data/tagVerb.txt", "r") as fp:
        for line in fp.readlines():
            if line.strip() == "": continue 		#skipping empty lines
            linelen = len(line)-1               	#removing \n 
            line = line[:linelen]
            dict[line] = "verb"    
    return dict




def tokenise_en(sent):
    sent = re.sub("([^ ])\'", r"\1 '", sent) 			# separate apostrophe from preceding word by a space if no space to left
    sent = re.sub(" \'", r" ' ", sent) 					# separate apostrophe from following word if a space if left

    # separate on punctuation
    cannot_precede = ["M", "Prof", "Sgt", "Lt", "Ltd", "co", "etc", "[A-Z]", "[Ii].e", "[eE].g"] # non-exhaustive list
    regex_cannot_precede = "(?:(?<!"+")(?<!".join(cannot_precede)+"))"
    sent = re.sub(regex_cannot_precede+"([\.\,\;\:\)\(\"\?\!]( |$))", r" \1", sent)
    sent = re.sub("((^| )[\.\?\!]) ([\.\?\!]( |$))", r"\1\2", sent) # then restick several fullstops ... or several ?? or !!
    sent = sent.split() 								# split on whitespace
    return sent


def tokenizeQuestion():
	return


#tokenize a given sentence, using nltk's word_tokenize 
def tokenizeSentence(sent):

	sentWordList = word_tokenize(sent)
	
	#affiche la liste des mots de la phrase
	#print("\nUeer said : ")
	#for s in sentWordList:
	#	print(s)

	return sentWordList


def botAnswer():
	return


def modeThree():
	return


if __name__=="__main__":
    listModeOne = []
    listModeOne = readDataLine("../data/dataModeOne.txt")
    answerModeOne = ""
    answerModeTwo = ""
    dictModeTwo = createDict()
    dictVerb = createDictVerb()
    user = ""
    
    answerAI = readDataLine("../data/dataModeTwoAnswers/answerAI.txt")
    answerCharacter = readDataLine("../data/dataModeTwoAnswers/answerCharacter.txt")
    answerInventory = readDataLine("../data/dataModeTwoAnswers/answerInventory.txt")
    answerEnvironment = readDataLine("../data/dataModeTwoAnswers/answerEnvironment.txt")
    answerInfo = readDataLine("../data/dataModeTwoAnswers/answerInfo.txt")

    while(user != "quit"):
        user = input("User: ")
        if user == "quit":
            printAnswer("Bye")
        else:
            sent = tokenise_en(user)
            answerModeTwo = modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo)
            if answerModeTwo != "":
                printAnswer(answerModeTwo)
            else:
                answerModeOne = modeOne(listModeOne, answerModeOne, None)
                printAnswer(answerModeOne)
        
