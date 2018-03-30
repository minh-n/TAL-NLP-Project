#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import re
import os
import random 


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
 
	return answer


def printAnswer(answer):
	print("\tBot: " + answer)


def modeTwo(sent, dicoModeTwo, answerModeTwo, answerAI, answerCharacter, answerEmotion, answerEnvironment, answerInfo):
    tag = None
    answer = ""
    
    for cle, value in dicoModeTwo.items():
        print("mot : {}, tag : {}".format(cle, value))
    for word in sent:
        print(word)
        if word in dicoModeTwo:
            tag = dicoModeTwo[word]
            break

    if tag != None:
        if tag == "tagAI.txt":
            answer = modeOne(answerAI, answerModeTwo)
        elif tag == "tagCharacter.txt":
            answer = modeOne(answerCharacter, answerModeTwo)
        elif tag == "tagEmotion.txt":
            answer = modeOne(answerEmotion, answerModeTwo)
        elif tag == "tagEnvironment.txt":
            answer = modeOne(answerEnvironment, answerModeTwo)
        else:
            answer = modeOne(answerInfo, answerModeTwo)
        
    return answer


def contains(word):
	return

def createDict():
    dico = {}
    for element in os.listdir("./data/dataModeTwo"):
        with open("./data/dataModeTwo/" + element, "r") as fp:
            for line in fp.readlines():
                if line.strip() == "": continue 	#skipping empty lines
                dico[line] = element	
        
    return dico

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

def tokenizeQuestion():
	return

def botAnswer():
	return


if __name__=="__main__":	

    listModeOne = []
    listModeOne = readDataLine("./data/dataModeOne.txt")
    answerModeOne = ""
    answerModeTwo = ""
    dicoModeTwo = createDict()
    user = ""
    
    answerAI = readDataLine("./data/dataModeTwoAnswers/answerAI.txt")
    answerCharacter = readDataLine("./data/dataModeTwoAnswers/answerCharacter.txt")
    answerEmotion = readDataLine("./data/dataModeTwoAnswers/answerEmotion.txt")
    answerEnvironment = readDataLine("./data/dataModeTwoAnswers/answerEnvironment.txt")
    answerInfo = readDataLine("./data/dataModeTwoAnswers/answerInfo.txt")

    while(user != "quit"):
        user = input("User: ")
        if user == "quit":
            printAnswer("Bye")
        else:
            sent = tokenise_en(user)
            answerModeTwo = modeTwo(sent, dicoModeTwo, answerModeTwo, answerAI, answerCharacter, answerEmotion, answerEnvironment, answerInfo)
            if answerModeTwo != "":
                printAnswer(answerModeTwo)
            else:
                answerModeOne = modeOne(listModeOne, answerModeOne)
                printAnswer(answerModeOne)
        
