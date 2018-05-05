#
#Computing bot answers
#

import random
import re
from itertools import permutations


#Compute an answer for mode one or two, depending on the input
def modeOne(listMode, previousAnswer, appendString):

	loop = True

	while(loop):
		answerNum = random.randint(0,len(listMode)-1)
		answer = listMode[answerNum]
		if(answer != previousAnswer):
			loop = False
		if(appendString != None):
			mystring = answer
			pattern = re.compile(r'<.+>')
			newstring = pattern.sub(appendString, mystring)
			answer = newstring
	
	return answer

#----------------------
#-------MODE TWO-------
#----------------------
#

#Compute an answer for the 'be' verb
def answerVerb(sentString, verb):
	ans = ""
	temp = []
	temp = andProb(sentString, temp)
	
	for eachPart in temp:
		if "I" in eachPart:
			tmp = " ".join(eachPart)
			if verb in tmp:

				buff = tmp[tmp.find(verb)+len(verb):]
				if buff[-1] == '.':		#removing '.' and '!'
					buff = buff[:-1]
				elif buff[-1] == '!':
					buff = buff[:-1]

				if verb == "m":
					ans = "Why are you" + buff + "?"
				elif verb == "am":
					ans = "Why are you" + buff + "?"
				elif verb == "was":
					ans = "Why were you" + buff + "?"
				elif verb == "am being":
					ans = "Why are you being" + buff + "?"
				elif verb == "have been":
					ans = "Why have you been" + buff + "?"
				elif verb == "will be":
					ans = "Why will you be" + buff + "?"
				elif verb == "will have been":
					ans = "Why will have you been" + buff + "?"
				elif verb == "was being":
					ans = "Why were you being" + buff + "?"
				elif verb == "had been":
					ans = "Why had you been" + buff + "?"
				elif verb == "will be being":
					ans = "Why will be you being" + buff + "?"
				elif verb == "have been being":
					ans = "Why have you been being" + buff + "?"
				elif verb == "had been being":
					ans = "Why had you been being" + buff + "?"
				elif verb == "will have been being":
					ans = "Why will have you been being" + buff + "?"
				else:
					print("DEBUG : answerVerb error (this line should not appear)!") 
				break

	return ans

#Recognizes several parts of a sentence, separated by 'and'
def andProb(sentString, temp):
	if "and" in sentString:
		firstPart = sentString[:sentString.index("and")]
		secondPart = sentString[-(len(sentString) - (sentString.index("and")+1)):]
		temp.append(firstPart)
		temp = andProb(secondPart, temp)
	else:
		temp.append(sentString)

	return temp

#The main mode 2 function
def modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo):
	tag = None
	answer = ""
	currentWord = ""

	sentStr = " ".join(sent)

	for key in dictVerb:
		if key in sentStr:
			answer = answerVerb(sent, key)

	if answer == "":
		for word in sent:
			if word in dictModeTwo:
				currentWord = word 				#an useful word is memorized
				tag = dictModeTwo[word]
				break

	if tag != None:								#computing the answer depending on its tag
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


#----------------------
#------MODE THREE------
#----------------------

#Returns every possible combinations of tags
#from a n-length list to a n-1-length list. 
def getlistPermutations(listTags):

	listPermut = []
	tagLen = len(listTags)
	if tagLen > 2:
		listPermut = list(permutations(listTags, tagLen-1))
	elif tagLen == 2:
		listPermut = list(permutations(listTags, 2))
	else:
		listPermut = listTags


	return listPermut

#Extracts tags from a sentence
def getTagsFromSent(sent, dictThreeLex):

	contextChar = ""
	contextPlace = ""

	listTags = []
	for word in sent:
		if word in dictThreeLex:
			listTags.append(dictThreeLex[word])

	return listTags

#Extracts the sentence's context
def getContextFromSent(sent, dictThreeLex, contextChar, contextPlace, contextObject):

	#updating context when needed

	whichState = ""
	for word in sent:
		if word in dictThreeLex:
			if dictThreeLex[word] == "character":
				word = word.title()
				contextChar = word
			elif dictThreeLex[word] == "room":
				contextPlace = word
			elif dictThreeLex[word] == "object":
				contextObject = word
			elif dictThreeLex[word] == "where":		#asking a question about the character's location
				contextPlace = ""					#reseting current room 

			elif dictThreeLex[word] == "sleep_state":
				whichState = "sleep_state"
			elif dictThreeLex[word] == "hydra_state":
				whichState = "hydra_state"
			elif dictThreeLex[word] == "death_state":
				whichState = "death_state"
			elif dictThreeLex[word] == "food_state":
				whichState = "food_state"
			elif dictThreeLex[word] == "mind_state":
				whichState = "mind_state"

	return (contextChar, contextPlace, contextObject, whichState)

#Finds the corresponding number for a
#given a list of tags. If there is none, -1 is returned.
def getNumberFromTagList(listTags, dictThreeTag):

	number = -1
	for key, value in dictThreeTag.items(): 		#key is a number between 0 and n
		if set(listTags) == set(value):
			number = key
			break

	#if no answer is found, we proceed with the program
	#and will remove some tags
	return number

#Computes an answer for mode three.
#This function is also able to find another corresponding list
#in case nothing is recognized at first.
def getAnswerFromNumber(number, dictThreeTag, dictThreeSentence, listTags, contextChar, contextPlace, contextObject):

	ansStr = "" 				 
	numberRoundTwo = -1									#in case we didn't find a suitable answer the first time

	if number < 0:
		#print("DEBUG : liste de tags introuvable. Relancement")
		listPermut = getlistPermutations(listTags)

		for element in listPermut:
			numberRoundTwo = getNumberFromTagList(element, dictThreeTag)
			if numberRoundTwo > 0:
				answer = dictThreeSentence.get(numberRoundTwo)
				ansStr = " ".join(answer)
				break
			elif numberRoundTwo < 0: 
				ansStr = ""								#no answer is found. We switch to mode 2 by returning an empty answer.
	else:
		answer = dictThreeSentence.get(number)
		ansStr = " ".join(answer)

	
	return ansStr

#Converts the state (a number) into an adjective
def nbToWord(number, whichState):

	string = ""
	if whichState == "sleep_state":
		string += "sleeping"
	else :
		if whichState == "food_state":
			string += "eating"
		else :
			string += " hydrated"

	if number > 7. :
		string += " well"
	else :
		if (number > 3.) & (number <= 7.) :
			string += " normally"

		else :
			string = "not "+string+" at all"

	return string

#Returns the state of a character depending on the state we want (whichState)
def getState(currentChar, whichState):

	simuState = ""

	if whichState == "sleep_state":
		simuState = nbToWord(currentChar.sleep, whichState)
	elif whichState == "hydra_state":
		simuState = nbToWord(currentChar.hydratation, whichState)
	elif whichState == "death_state":
		if currentChar.alive == True:
			simuState = "alive"
		else:
			simuState = "dead"
	elif whichState == "food_state":
			simuState = nbToWord(currentChar.nutrition, whichState)
	elif whichState == "mind_state":
			simuState = currentChar.mind

	return simuState

#Links the story with the chatbot. This function extracts data from the story, injecting it into the bot's answer's %tokens 
def storyLink(answer, characters, rooms, contextChar, contextPlace, contextObject, whichState, contextState):

	if whichState == "":
		if contextState != "":
			whichState = contextState
	else:
		contextState = whichState

	simuState = ""
	simuYesno = ""
	simuAction = ""
	charFeatures = ""
	simuTopic = ""
	simuLocation = contextPlace

	#Antoine
	if contextChar == "Antoine":
		currentChar = characters[0]
		simuState = getState(currentChar, whichState)
		simuLocation = currentChar.location.name
		charFeatures = "a young man, late twenties. He likes chocolate cake and the movie \"The Room\"" 
		simuTopic = currentChar.conv

	#Laura
	elif contextChar == "Laura":
		currentChar = characters[1]
		simuState = getState(currentChar, whichState)
		simuLocation = currentChar.location.name
		charFeatures = "Miss Polytech 2017, she was sent to this house to seek the Holy Grail" 
		simuTopic = currentChar.conv

	#Maria
	elif contextChar == "Maria":
		currentChar = characters[2]
		simuState = getState(currentChar, whichState)
		simuLocation = currentChar.location.name
		charFeatures = "a 17-year-old high school girl. It seems that she likes Scott Pilgrim" 
		simuTopic = currentChar.conv

	#Annie
	elif contextChar == "Annie":
		currentChar = characters[3]
		simuState = getState(currentChar, whichState)
		simuLocation = currentChar.location.name
		charFeatures = "secretly a Titan, but shhhh." 
		simuTopic = currentChar.conv

	#Jeffery
	elif contextChar == "Jeffery":
		currentChar = characters[4]
		simuState = getState(currentChar, whichState)
		simuLocation = currentChar.location.name
		charFeatures = "a pro Hearthstone player. He likes to play even if he has a project to turn in for tomorrow" 
		simuTopic = currentChar.conv

	#replacing regex with context and inputs
	pattern = re.compile(r'\%char')
	answer = pattern.sub(contextChar, answer)

	pattern = re.compile(r'\%state')
	answer = pattern.sub(simuState, answer)

	patternYes = re.compile(r'\%yesno')
	patternPlace = re.compile(r'\%room')

	if simuLocation == contextPlace:		#character is in contextPlace
		answer = patternYes.sub("", answer)
		answer = patternPlace.sub(simuLocation, answer)
	elif contextPlace == "":
		answer = patternYes.sub("", answer)
		answer = patternPlace.sub(simuLocation, answer)
	else:									#character is not in contextPlace
		answer = patternYes.sub("not", answer)
		answer = patternPlace.sub(contextPlace, answer)

	pattern = re.compile(r'\%features')
	answer = pattern.sub(charFeatures, answer)

	pattern = re.compile(r'\%topic')
	answer = pattern.sub(simuTopic, answer)

	return answer, contextState

#The main mode 3 function
def modeThree(sent, characters, rooms, dictThreeLex, dictThreeTag, dictThreeSentence, contextChar, contextPlace, contextObject, contextState):

	listTags = []

	whichState = ""

	contextChar, contextPlace, contextObject, whichState = getContextFromSent(sent, dictThreeLex, contextChar, contextPlace, contextObject)

	listTags = getTagsFromSent(sent, dictThreeLex)

	number = getNumberFromTagList(listTags, dictThreeTag)
	answer = getAnswerFromNumber(number, dictThreeTag, dictThreeSentence, listTags, contextChar, contextPlace, contextObject)

	answer, contextState = storyLink(answer, characters, rooms, contextChar, contextPlace, contextObject, whichState, contextState)
	
	#Debug
	#print("this sentence's tagList:")
	#print(listTags)

	return answer, contextChar, contextPlace, contextObject, contextState



