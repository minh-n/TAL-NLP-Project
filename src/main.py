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

	#the conversation's context, used to replace the regex in the bot's answers in mode3
	contextChar = ""
	contextPlace = ""
	contextObject = ""


	#iterator to link the user input to the story
	count_input = 0

	#controller of the story, and point of acces to data :
	c = story.Controller()
	characters = c.environment.characters
	rooms = c.environment.rooms

	#main while loop
	while(user != "quit"): 			
		user = input("User: ")	#the user will be able to quit the program by typing 'quit'
		user = user.lower()
		if user == "quit":
			printAnswer("Goodbye!")
		else:
			sent = parser.tokenizeSentence(user) 	#the user's sentence is tokenized

			answerModeThree, contextChar, contextPlace, contextObject = compute.modeThree(sent, characters, rooms, dictThreeLex, dictThreeTag, dictThreeSentence, contextChar, contextPlace, contextObject)
			if answerModeThree != "": 				#if a mode3 answer is returned
				printAnswer(answerModeThree)
				#print("CurrentMode=3")
			else:									#else, we switch to mode 2
				answerModeTwo = compute.modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo)
				if answerModeTwo != "":				#if a mode2 answer is returned
					printAnswer(answerModeTwo)
					#print("CurrentMode=2")

				else:								#else, we switch to mode 1
					answerModeOne = compute.modeOne(listModeOne, answerModeOne, None)
					printAnswer(answerModeOne)
					#print("CurrentMode=1")


		if count_input%2 == 0 :
			c.timeForward(1)
