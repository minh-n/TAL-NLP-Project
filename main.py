#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random 

listModeOne = ["hmm", "ehh", "ahh", "ok", "lol", "yes", "right", "good", "huhu", "haha"]

answerModeOne = ""

def modeOne():

	global answerModeOne
	
	x = input("User: ")

	loop = True

	while(loop):
		answerNum = random.randint(0,len(listModeOne)-1)
		answer = listModeOne[answerNum]
		if(answer != answerModeOne):
			loop = False

	print("Bot: " + answer)
 
	answerModeOne = answer


if __name__=="__main__":	
	
	while(True):
		modeOne()