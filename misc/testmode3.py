def createDictThree:
	dict = {}
	for element in os.listdir("../data/dataModeThree"):
		with open("../data/dataModeThree/" + element, "r") as fp:
			for line in fp.readlines():
				if line.strip() == "": continue 		#skipping empty lines
				linelen = len(line)-1               	#removing \n 
				ine = line[:linelen]
				dict[line] = element    
	return dict


def tagSentModeThree(sent, dictVerb, dictModeThree, answerModeTwo, answerAI, answerCharacter, answerInventory, answerEnvironment, answerInfo):
	tagList = None
	answer = ""
	
	currentWord = ""

	context="" #???

	for word in sent:
		if word in dictModeThree:
			tagList = tagList.append(dictModeThree[word])

	if tag != None:						#computing the answer depending on its tag
		
		print("List des tags = " + tagList)

		answer, context = answerModeThree(tagList, context)  #answerModeThree will compute an answer with a given list of tags
	
	return answer


def answerModeThree(tagList, context):
	
	#find a specific answer, with the closest matching value with the tagList 


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
	
	return answer, context


def createTagList():

	dictTagList = {}
	with open("../data/answerModeThree/answer.txt", "r") as fp:
		for line in fp.readlines():
			if line.strip() == "": continue 		#skipping empty lines
			
			linelen = len(line)-1               	#removing \n
			line = line[:linelen]
			
			#here we should be able to recognize each tag
			#we should put the tags into a list
			#and the sentence into a string
			#and then combine the two somehow


			patternTagList = re.compile(r'<.+>')			

			patternTag = re.compile(r'{.+}')			



			dictTagList[line] = element


	return dictTagList


def dispTagList:
	return


