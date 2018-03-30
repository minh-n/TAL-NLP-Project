#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
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

	printAnswer(answer)
 
	return answer


def printAnswer(answer):
	print("\tBot: " + answer)



def modeTwo():
	return


def contains(word):
	return

def createDict():
	return


def tokenizeQuestion():
	return

def botAnswer():
	return


if __name__=="__main__":	

	listModeOne = []
	listModeOne = readDataLine("./data/dataModeOne.txt")
	answerModeOne = ""

	while(True):
		x = input("User: ")
		answerModeOne = modeOne(listModeOne, answerModeOne)
