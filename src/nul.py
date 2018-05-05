

def nbToWord(tag, state):
	string = ""
	if tag == "sleep_state":
		string += "sleeping"
	else :
		if tag == "food_state":
			string += "eating"
		else :
			string += "hydrated"

	if state > 7 :
		string += " well"
	else :
		if state > 3 & <= 7 :
			string += "normally"

		else :
			string = "not "+string+" at all"

	return string