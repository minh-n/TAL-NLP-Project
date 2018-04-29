#
#Computing bot answers
#

import random

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
	
	#for part in temp:
	#	print(part)

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

#
def andProb(sentString, temp):
	if "and" in sentString:
		firstPart = sentString[:sentString.index("and")]
		secondPart = sentString[-(len(sentString) - (sentString.index("and")+1)):]
		temp.append(firstPart)
		temp = andProb(secondPart, temp)
	else:
		temp.append(sentString)

	return temp

#
def modeTwo(sent, dictVerb, dictModeTwo, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo):
	tag = None
	answer = ""
	
	currentWord = ""

	#for cle, value in dictModeTwo.items(): #test print
		#print("mot : {}, tag : {}".format(cle, value))

	sentStr = " ".join(sent)

	for key in dictVerb:
		if key in sentStr:
			answer = answerVerb(sent, key)

	if answer == "":
		for word in sent:
			if word in dictModeTwo:
				currentWord = word 		#an useful word is memorized
				tag = dictModeTwo[word]
				break

	if tag != None:				#computing the answer depending on its tag
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

#?
def contains(word):
	return

#?
def modeThree():
	return

