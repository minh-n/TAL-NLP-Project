import story_aux as s


class Controller:
	def __init__(self):
		self.environment = s.Environment()
		self.time = 0
		f = open("output_status.txt", "w")
		f.close()

#Code clarity functions

	#select a character via its name
	def c(self, nam):
		for x in self.environment.characters:
			if x.name == nam:
				return x

		#print("ERROR : can't select character, no char has this name")
		return None

	#select a room via its name
	def r(self, nam):
		for x in self.environment.rooms:
			if x.name == nam:
				return x

		#print("ERROR : can't select room, no room has this name")
		return None


#Control functions

	#write all needed info about the status of the simulation
	def updateOutput(self):
		f = open("output_status.txt", "w")

		f.write("CHARACTERS:\n\n")
		for x in self.environment.characters:
			f.write(x.name+"\n")
			f.write(x.eekname+"\n")
			if x.alive :
				f.write("alive\n")
			else :
				f.write("dead\n")
			f.write(x.location.name+"\n")

			nothing=True
			for item in x.inventory.tools:
				f.write(item.name+" ")
				nothing=False
			for item in x.inventory.entertainments:
				f.write(item.name+" ")
				nothing=False
			for item in x.inventory.ressources:
				f.write(item.name+" ")
				nothing=False
			if nothing == True:
				f.write("*")
			f.write("\n")

			f.write(x.mind+"\n")
			f.write(str(x.nutrition)+"\n")
			f.write(str(x.hydration)+"\n")
			f.write(str(x.sleep)+"\n")

			for info in x.relationships:
				f.write(str(info)+"\n")
			f.write("\n")

		f.write("ROOMS:\n\n")
		for x in self.environment.rooms:
			f.write(x.name+"\n")

			nothing = True
			for people in x.inhabitants:
				f.write(people.name+" ")
				nothing = False
			if nothing == True:
				f.write("*")
			f.write("\n")

			nothing = True
			for item in x.inventory.tools:
				f.write(item.name+" ")
				nothing=False
			for item in x.inventory.entertainments:
				f.write(item.name+" ")
				nothing=False
			for item in x.inventory.ressources:
				f.write(item.name+" ")
				nothing=False
			if nothing == True:
				f.write("*")
			f.write("\n")

			f.write(x.state+"\n")
			if x.closed == True:
				f.write("closed\n\n")
			else:
				f.write("opened\n\n")
			#todo : inventory and inhabitants?

		f.write("OBJECTS:\n\n")
		f.write("gun\n")
		f.write(self.search("gun").name)

		f.close()

	#next step of the simulation
	def timeForward(self, nb):
		self.time += nb

		for i in range (0, nb):
			for x in self.environment.characters:
				if x.alive == True:
					x.act(self)

		self.updateOutput()
			

	#search and return an object when given its name
	#not used everywhere because greedy
	def search(self, is_searched):
		for x in self.environment.rooms:
			for item in x.inventory.tools:
				if item.name==is_searched:
					return x

		for x in self.environment.rooms:
			for item in x.inventory.entertainments:
				if item.name==is_searched:
					return x

		for x in self.environment.rooms:
			for item in x.inventory.ressources:
				if item.name==is_searched:
					return x

		for x in self.environment.characters:
			for item in x.inventory.tools:
				if item.name==is_searched:
					return x


		for x in self.environment.characters:
			for item in x.inventory.ressources:
				if item.name==is_searched:
					return x

		for x in self.environment.characters:
			for item in x.inventory.entertainments:
				if item.name==is_searched:
					return x

		#print("subForward : can't find object")
		return None

'''

	# what : string / how : int
	def changeTools(self, where, what, how):
		target = None
		for x in self.environment.characters:
			if x.name == where:
				target = x

		if target == None:
			for x in self.environment.rooms:
				if x.name == where:
					target = x

		if target == None:
			print("ERROR : can't change tool, incorrect where")

		for x in target.inventory.tool:
			if x.name == what:
				if how == -1:


		return 0


	def changeEntertainment():
		return 0


	def changeRessources():
		return 0


	def changeCharacter():
		return 0

'''




'''
#test MAIN
print("\n")

c = Controller()

while input("q to quit\n") != "q" :
	c.timeForward(1)

print("\n")







NOTES :
Si le perso interagit avec un truc qui n'est pas dans sa pièce,
on doit vérifier qu'il peut y aller, et il y move.

Rajouter une quantité dans la fonction consume

What about taking water?

The order of rooms and characters are important

Relationship avec soit même est miajour de manière débile

Nothing changes the state of a room :/

'''