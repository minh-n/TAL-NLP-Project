#
#
#

import os
import re

#Reads lines from a file and storing them into a list.
def readDataLine(fname):

	linesRead = []	
	with open(fname, "r") as fp:						#file opening
		for line in fp.readlines():
			if line.strip() == "": continue 			#skipping empty lines
			linesRead.append(line)	

	return linesRead

#----------------------
#-------MODE TWO-------
#----------------------

#Creates a dictionary of every words from each of the 5 txt files
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

#Creates a dictionary of 'be' verbs (am, are, is...)
def createDictVerb():
	dict = {}
	with open("../data/tagVerb.txt", "r") as fp:
		for line in fp.readlines():
			if line.strip() == "": continue 			#skipping empty lines
			linelen = len(line)-1               		#removing \n 
			line = line[:linelen]
			dict[line] = "verb"    
	return dict

#Creates a dictionary of subjects (I, you...)
#----------------UNUSED !!!!!!
def createDictSubject():
	dict = {}
	with open("../data/tagSubject.txt", "r") as fp:
		for line in fp.readlines():
			if line.strip() == "": continue 			#skipping empty lines
			linelen = len(line)-1               		#removing \n 
			line = line[:linelen]
			dict[line] = "subject"    
	return dict


#----------------------
#------MODE THREE------
#----------------------

#Extracts tag
def extractTag(line):
	tag = re.findall('<\S+>', line)
	tagClean = []

	for string in tag:		#removing < and >
		string = re.sub('<', '', string)
		string = re.sub('>', '', string)
		tagClean.append(string)

	#if len(tagClean)>0: 
	#	print("debugTAGS : ")
	#	print(tagClean)

	return tagClean

#
def extractSentence(line):
	sentence = re.findall('{.+}', line)
	sentenceClean = []
	for string in sentence:		#removing { and }
		string = re.sub('{', '', string)
		string = re.sub('}', '', string)
		sentenceClean.append(string)

	#print("debugSENTENCES : ")
	#print(sentenceClean)
	return sentenceClean

#mode three
def createDictTagList():

	dictTagList = {}
	with open("../data/dataModeThreeAnswers/botPhrases.txt", "r") as fp:
		for line in fp.readlines():
			if line.strip() == "": continue 			#skipping empty lines
			
			linelen = len(line)-1               		#removing \n
			line = line[:linelen]
			
			#here we should be able to recognize each tag
			#we should put the tags into a list
			#and the sentence into a string
			#and then combine the two somehow

			tag = extractTag(line)
			sentence = extractSentence(line)
	return dictTagList
