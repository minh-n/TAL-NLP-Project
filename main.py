#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random 


def read_data_line(fname):

    linesRead = []
    	
    #ouverture automatique du fichier
    with open(fname, "r") as fp:

        for line in fp.readlines():
            if line.strip() == "": continue 	#on saute les lignes vides
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



if __name__=="__main__":	

	listModeOne = []
	listModeOne = read_data_line("./data/dataModeOne.txt")
	answerModeOne = ""

	while(True):
		x = input("User: ")
		answerModeOne = modeOne(listModeOne, answerModeOne)
