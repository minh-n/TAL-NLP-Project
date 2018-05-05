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

	#creating dictionaries for mode2
	dictModeTwo = data.createDict()
	dictVerb = data.createDictVerb()

	#creating dictionaries for mode3
	dictThreeLex = data.createDictThreeLex()
	dictThreeTag, dictThreeSentence = data.createDictTagSent()
	
	#the different answers for mode2
	answerAI = data.readDataLine("../data/dataModeTwoAnswers/answerAI.txt")
	answerCharacter = data.readDataLine("../data/dataModeTwoAnswers/answerCharacter.txt")
	answerInventory = data.readDataLine("../data/dataModeTwoAnswers/answerInventory.txt")
	answerEnvironment = data.readDataLine("../data/dataModeTwoAnswers/answerEnvironment.txt")
	answerInfo = data.readDataLine("../data/dataModeTwoAnswers/answerInfo.txt")

	#the user's input
	user = ""

	#main while loop
	while(user != "quit"): 			
		user = raw_input("User: ")	#the user will be able to quit the program by typing 'quit'
		if user == "quit":
			printAnswer("Goodbye!")
		else:
			sent = parser.tokenizeSentence(user) 	#the user's sentence is tokenized

			answerModeThree = compute.modeThree(sent, dictThreeLex, dictThreeTag, dictThreeSentence)
			if answerModeThree != "": 				#if a mode3 answer is returned
				printAnswer(answerModeThree)
				print("CurrentMode=3")
			else:									#else, we switch to mode 2
				answerModeTwo = compute.modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo)
				if answerModeTwo != "":				#if a mode2 answer is returned
					printAnswer(answerModeTwo)
					print("CurrentMode=2")

				else:								#else, we switch to mode 1
					answerModeOne = compute.modeOne(listModeOne, answerModeOne, None)
					printAnswer(answerModeOne)
					print("CurrentMode=1")

			
