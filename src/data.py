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

#Removing \n at the end of each word
def removeEndLine(word):
	linelen = len(word)
	if word[linelen-1] == '\n':				#removing \n 
		linelen = len(word)-1               	
		word = word[:linelen]
	return word

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
				line = removeEndLine(line)

				dict[line] = element    
	return dict

#Creates a dictionary of 'be' verbs (am, are, is...)
def createDictVerb():
	dict = {}
	with open("../data/tagVerb.txt", "r") as fp:
		for line in fp.readlines():
			if line.strip() == "": continue 			#skipping empty lines
			line = removeEndLine(line)

			dict[line] = "verb"    
	return dict

#Creates a dictionary of subjects (I, you...)
#---------------------------------------------------UNUSED !!!!!!
def createDictSubject():
	dict = {}
	with open("../data/tagSubject.txt", "r") as fp:
		for line in fp.readlines():
			if line.strip() == "": continue 			#skipping empty lines
			line = removeEndLine(line)

			dict[line] = "subject"    
	return dict


#----------------------
#------MODE THREE------
#----------------------

#Creates a dictionary of every words from each of the mode3's txt files
def createDictThreeLex():
	dictThreeLex = {}

	for tag in os.listdir("../data/dataModeThree"):
		if not tag.startswith('.'):
			with open("../data/dataModeThree/" + tag, "r") as fp:
				for word in fp.readlines():
					if word.strip() == "": continue 		#skipping empty lines
					
					word = removeEndLine(word)

					tag = tag.replace(".txt", "")			#removing .txt from tag names
					dictThreeLex[word] = tag

	return dictThreeLex

#Extracts tags from a <tag1> <tag2> {sentence} line
def extractTag(line):
	tag = re.findall('<\S+>', line)
	tagClean = []

	for string in tag:		#removing < and >
		string = re.sub('<', '', string)
		string = re.sub('>', '', string)
		tagClean.append(string)
	return tagClean

#Extracts a sentence from a <tag1><tag2>{sentence} line
def extractSentence(line):
	sentence = re.findall('{.+}', line)
	sentenceClean = []
	for string in sentence:		#removing { and }
		string = re.sub('{', '', string)
		string = re.sub('}', '', string)
		sentenceClean.append(string)
	return sentenceClean

#Creates a dictionary from tags and sentences
def createDictTagSent():

	dictThreeTag = {}
	dictThreeSentence = {}
	count = 0

	with open("../data/dataModeThreeAnswers/botPhrases.txt", "r") as fp:
		for line in fp.readlines():
			if line.strip() == "": continue 			#skipping empty lines
			
			line = removeEndLine(line)
			
			tag = extractTag(line) 						#recognizing each tag
			sentence = extractSentence(line)

			dictThreeTag[count] = tag 					#separating the two:
			dictThreeSentence[count] = sentence 		#one dict for the tags and one for the sentence
			count = count + 1 					  		#each have the same counter

	return (dictThreeTag, dictThreeSentence)
