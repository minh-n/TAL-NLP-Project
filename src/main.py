#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import re
import os

import parser
import data
import compute
import story

#to run the program using NLTK, downloading an extra package may be needed:
#(python/py3) -m nltk.downloader 'punkt'

def printAnswer(answer):
	print("\tBot: " + answer)


if __name__=="__main__":
	listModeOne = []
	listModeOne = data.readDataLine("../data/dataModeOne.txt")
	answerModeOne = ""
	answerModeTwo = ""
	dictModeTwo = data.createDict()
	dictVerb = data.createDictVerb()
	user = ""
	
	answerAI = data.readDataLine("../data/dataModeTwoAnswers/answerAI.txt")
	answerCharacter = data.readDataLine("../data/dataModeTwoAnswers/answerCharacter.txt")
	answerInventory = data.readDataLine("../data/dataModeTwoAnswers/answerInventory.txt")
	answerEnvironment = data.readDataLine("../data/dataModeTwoAnswers/answerEnvironment.txt")
	answerInfo = data.readDataLine("../data/dataModeTwoAnswers/answerInfo.txt")

	dictTag = data.createDictTagList()

	while(user != "quit"):
		user = raw_input("User: ")
		if user == "quit":
			printAnswer("Bye")
		else:
			sent = parser.tokenizeSentence(user)
			answerModeTwo = compute.modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo)
			if answerModeTwo != "":
				printAnswer(answerModeTwo)
			else:
				answerModeOne = compute.modeOne(listModeOne, answerModeOne, None)
				printAnswer(answerModeOne)
		
