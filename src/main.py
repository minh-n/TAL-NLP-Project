#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import re
import os
import random as r

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

	listModeOneExtra = []
	listModeOneExtra = data.readDataLine("../data/dataModeOneExtra.txt")
	answerModeOneExtra = ""

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
	userMenu = ""

	#the conversation's context, used to replace the regex in the bot's answers in mode3
	contextChar = ""
	contextPlace = ""
	contextObject = ""
	contextState = ""

	#iterator to link the user input to the story
	count_input = 0

	#controller of the story, and point of acces to data :
	c = story.Controller()
	characters = c.environment.characters
	rooms = c.environment.rooms


	#main while loop
	while(userMenu != "quit"):
		print("\n\n--------------------\n\n")
		print("I'm Storybot and I will tell you a story. Please choose between 1, 2 or 3. Type \"quit\" if you want to exit.")
		print("1: the story mode.")
		print("2: some background for the story.")
		print("3: technical details about this project.")
		print("quit: exit the program.\n")
		userMenu = input("Your choice: ")
		print("\n")
		if userMenu == '1':
			print("\n\n---------STORY MODE---------\n\n")

			print("\nMaria, Annie, Antoine, Jeffery and Laura are stuck in a house. Discover their story... or type quit to go back.")
			print("You can ask me a question about who they are, their state of mind, their location or their inventory.\n")
			while(user != "quit"):
				user = input("You: ")	#the user will be able to quit the program by typing 'quit'
				user = user.lower()
				previousAnswer = ""
				previousAnswerExtra = ""

				if user == "quit":
					printAnswer("Goodbye!")
				else:
					sent = parser.tokenizeSentence(user) 	#the user's sentence is tokenized

					answerModeThree, contextChar, contextPlace, contextObject, contextState = compute.modeThree(sent, characters, rooms, dictThreeLex, dictThreeTag, dictThreeSentence, contextChar, contextPlace, contextObject, contextState)
					if answerModeThree != "": 				#if a mode3 answer is returned
							
						if r.randint(0,2) == 0:
							#randomly prints backchannels from mode one
							answerModeOne = compute.modeOne(listModeOne, previousAnswer, None)
							answerModeOne = data.removeEndLine(answerModeOne)
							previousAnswer = answerModeOne
							printAnswer(answerModeOne)

						printAnswer(answerModeThree)

						if r.randint(0,3) == 0:
							#another series of backchannels to make the conversation more lively!
							answerModeOneExtra = compute.modeOne(listModeOneExtra, previousAnswerExtra, None)
							answerModeOneExtra = data.removeEndLine(answerModeOneExtra)
							previousAnswerExtra = answerModeOneExtra
							printAnswer(answerModeOneExtra)

						#print("CurrentMode=3")
					else:									#else, we switch to mode 2
						answerModeTwo = compute.modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo)
						if answerModeTwo != "":				#if a mode2 answer is returned
							printAnswer(answerModeTwo)
							#print("CurrentMode=2")

						else:								#else, we switch to mode 1
							answerModeOne = compute.modeOne(listModeOne, answerModeOne, None)
							answerModeOne = data.removeEndLine(answerModeOne)
							printAnswer(answerModeOne)
							#print("CurrentMode=1")


				if count_input%2 == 0 :
					c.timeForward(1)
		elif userMenu == '2':
			print("\n\n--------STORY BACKGROUND---------\n\n")
			print("Maria, Annie, Antoine, Jeffery and Laura are stuck in a house. They're interacting with each other and figuring out how to survive.")
			print("\nIt seems like a powerful AI is watching every of their steps, and influencing them in their daily lives...\n\n\n")
		elif userMenu == '3':
			print("\n\n--------TECHNICAL DETAILS---------\n\n")

			print("The chatbot is able to answer using three modes.\nMode 3 is the main story mode. It uses a system of tags: the user's input sentece is associated with a list of tags generated from a database of about 60 tags. This list is used to find a suitable answer in another database which contains several answers, each one corresponding to a tag list.")

			print("\nMode 2 is a simplified Mode 3 : in case Mode 3 is not able to compute an answer, Mode 2 will give a simpler answer by re-associating the same sentence with only one tag.")

			print("\nMode 1 does not use tag recognition and whatever the user says, the chatbot will answer with 'backchannels', such as `Uhh..` or `Hmm…`.")

			print("\nFurther explanations can be found in French (`/misc/Rapport.pdf`).\n\n\n")




