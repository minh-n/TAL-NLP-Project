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
	temp = []
	temp = andProb(sentString, temp)

	for eachPart in temp:
		if "I" in eachPart:
			if verb in eachPart:
				buff = eachPart[eachPart.index(verb) + len(verb):]
				buff = ' '.join(buff)

				if verb == "am":
					ans = "Why are you " + buff + "?"
				elif verb == "was":
					ans = "Why were you " + buff + "?"
				elif verb == "am being":
					ans = "Why are you being " + buff + "?"
				elif verb == "have been":
					ans = "Why have you been " + buff + "?"
				elif verb == "will be":
					ans = "Why will you be " + buff + "?"
				elif verb == "will have been":
					ans = "Why will have you been " + buff + "?"
				elif verb == "was being":
					ans = "Why were you being " + buff + "?"
				elif verb == "had been":
					ans = "Why had you been " + buff + "?"
				elif verb == "will be being":
					ans = "Why will be you being " + buff + "?"
				elif verb == "have been being":
					ans = "Why have you been being " + buff + "?"
				elif verb == "had been being":
					ans = "Why had you been being " + buff + "?"
				elif verb == "will have been being":
					ans = "Why will have you been being " + buff + "?"
				else:
					print("DEBUG : answerVerb error (this line should not appear)!") 
				break


	return ans


def andProb(sentString, temp):
	if "and" in sentString:
		firstPart = sentString[:sentString.index("and")]
		secondPart = sentString[-(len(sentString) - sentString.index("and") - 4):]
		temp.append(firstPart)
		temp = andProb(secondPart, temp)
	else:
		temp.append(sentString)

	return temp



def printAnswer(answer):
	print("\tBot: " + answer)


def modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo):
    tag = None
    answer = ""
    
    currentWord = ""

    #for cle, value in dictModeTwo.items():
        #print("mot : {}, tag : {}".format(cle, value))

    sentStr = " ".join(sent)

    for key in dictVerb:
    	if key in sentStr:
    		answer = answerVerb(sent, key)
    		break

    if answer == "":
        for word in sent:
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


def createDictSubject():
    dict = {}
    with open("../data/tagSubject.txt", "r") as fp:
        for line in fp.readlines():
            if line.strip() == "": continue 		#skipping empty lines
            linelen = len(line)-1               	#removing \n 
            line = line[:linelen]
            dict[line] = "subject"    
    return dict



def tokenizeQuestion():
	return


#tokenize a given sentence, using nltk's word_tokenize 
def tokenizeSentence(sent):

	sentWordList = word_tokenize(sent)

	return sentWordList


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
            sent = tokenizeSentence(user)
            answerModeTwo = modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo)
            if answerModeTwo != "":
                printAnswer(answerModeTwo)
            else:
                answerModeOne = modeOne(listModeOne, answerModeOne, None)
                printAnswer(answerModeOne)
        
