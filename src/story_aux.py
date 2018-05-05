import random as r

'''

depressed : low chance to kill itself or kill someone they don't like
won't talk to anyone
won't entertain themselves
Stay in their room

apathetic : will talk to someone they like
will entertain sometimes with books.
sometimes won't eat

neutral : will try to talk to anyone

joyful : will cheerup anyone, but it might hurt them

determined : won't sleep
might kill someone they really don't like
will eat again if not full


the talk function :
generate a random subject of conversation

generate a random outcome of the conversation

can't be affected regarding why the conversation takes place



'''

state_room_enum = ["tidy", "neutral", "messy", "chaos", "unusable"]

mind_enum = ["depressed", "apathetic", "neutral", "joyful", "determined"]

rand_conv_enum = ["the movie The Room", "existencialism", "what the forest smells like", "the rules of Cards against humanity"]
cheruup_enum = ["the time he/she cooked for everyone, and it was delicious", "everybody loving to be around him/her"]
real_talk_enum = ["what they think of Jeffery", "how painful it is to listen to Annie talk for hours", "how much they hate this closed space"]



class Environment:
	def __init__(self):	
		self.rooms = [] #will be a list of Room
		
		self.rooms.append(Room("living room"))
		self.rooms[-1].inventory.tools.append(Tool("gun"))
		self.rooms[-1].inventory.entertainments.append(Entertainment("TV", 2))
		self.rooms[-1].inventory.entertainments.append(Entertainment("deck_of_cards", 1))
		self.rooms[-1].inventory.entertainments.append(Entertainment("Catcher_in_the_rye", 2))
		self.rooms[-1].inventory.entertainments.append(Entertainment("Millenium", 2))
		self.rooms[-1].inventory.ressources.append(Ressource("water", [("hydration", 2)], 5))
		self.rooms[-1].inventory.ressources.append(Ressource("food", [("nutrition", 2)], 5))

		self.rooms.append(Room("roof"))
		self.rooms[-1].inventory.tools.append(Tool("crowbar"))	
		self.rooms[-1].inventory.entertainments.append(Entertainment("the_view", 1))

		self.rooms.append(Room("bathroom"))
		self.rooms[-1].inventory.ressources.append(Ressource("water", [("hydration", 1)], -1))

		self.rooms.append(Room("kitchen"))
		self.rooms[-1].inventory.ressources.append(Ressource("water", [("hydration", 1)], -1))
		self.rooms[-1].inventory.tools.append(Tool("knife"))
		self.rooms[-1].inventory.ressources.append(Ressource("food", [("nutrition", 2),("mind",0.5)], 50))
		self.rooms[-1].inventory.ressources.append(Ressource("good_food", [("nutrition", 2),("mind",1)], 10))

		self.rooms.append(Room("toilets"))
		self.rooms[-1].inventory.tools.append(Tool("flashlight"))
		self.rooms[-1].inventory.tools.append(Tool("rifle"))
		self.rooms[-1].inventory.ressources.append(Ressource("water", [("hydration", 1)], -1))

		self.rooms.append(Room("bedroom Antoine"))

		self.rooms.append(Room("bedroom Laura"))

		self.rooms.append(Room("bedroom Maria"))
		self.rooms[-1].inventory.entertainments.append(Entertainment("CRT_TV", 1))

		self.rooms.append(Room("bedroom Annie"))

		self.rooms.append(Room("bedroom Jeffery"))
		self.rooms[-1].inventory.entertainments.append(Entertainment("War_and_peace", 1))



		self.characters = []  #will be a list of Character
		self.characters.append(Character("m","Antoine", "Aaronson", self.rooms[0]))
		self.characters.append(Character("m","Laura", "Llorar", self.rooms[0]))
		self.characters.append(Character("m","Maria", "Xu", self.rooms[0]))
		self.characters.append(Character("m","Annie", "Wiseau", self.rooms[0]))
		self.characters.append(Character("m","Jeffery", "Jafar", self.rooms[0]))

class Character:

	#gen : letter / name,eek : strings / loc : Room
	def __init__(self, gen, nam, eek, loc):
		self.gender = gen
		self.name = nam
		self.eekname = eek
		self.location = loc
		self.inventory = Inventory()
		self.mind = mind_enum[2]
		self.nutrition = 5
		self.hydration = 5
		self.sleep = 5
		self.relationships = [3,3,3,3,3]
		self.alive = True

		loc.inhabitants.append(self)


	#room : Room
	def move(self, room):
		self.location.inhabitants.remove(self)
		room.inhabitants.append(self)
		self.location = room

		#but he may not be able to move


	#type : string / obj : Ressource or Tool or Entertainment
	def take(self, name):
		found = 0
		for x in self.location.inventory.tools:
			if x.name == name:
				self.inventory.tools.append(x)
				self.location.inventory.tools.remove(x)
				found = 1

		if found == 0:
			for x in self.location.inventory.ressources:
				if x.name == name:
					self.inventory.ressources.append(x)
					self.location.inventory.ressources.remove(x)
					found = 1

		if found == 0:
			for x in self.location.inventory.entertainments:
				if x.name == name:
					self.inventory.entertainments.append(x)
					self.location.inventory.entertainments.remove(x)
					found = 1

		#if found == 0:
			#print("ERROR : object can't be picked up : object not found")

		#might have other effects
		


	#obj : Ressource or Tool or Entertainment
	def drop(self, name):
		found = 0
		for x in self.inventory.tools:
			if x.name == name:
				self.location.tools.append(x)
				self.inventory.tools.remove(x)
				found = 1

		if found == 0:
			for x in self.inventory.ressources:
				if x.name == name:
					self.location.ressources.append(x)
					self.inventory.ressources.remove(x)
					found = 1

		if found == 0:
			for x in self.inventory.entertainments:
				if x.name == name:
					self.location.entertainments.append(x)
					self.inventory.entertainments.remove(x)
					found = 1

		#if found == 0:
			#print("ERROR : object can't be removed : object not found")


	def alterRoom(self, state):
		if state in state_room_enum:
			self.location.state = state
		#else:
			#print("ERROR : can't change state : unacceptable state ")



	#ent : Entertainment.effect
	def entertain(self, effect):
		s = self.mind
		for x in mind_enum:
			if x == s:
				index = mind_enum.index(x)
		index += effect
		if index >= len(mind_enum):
			index = len(mind_enum)-1
		else: 
			if index < 0:
				index = 0

		self.mind = mind_enum[index]
		return 0

	
	#res : Ressources / q : int / loc : wherever the ressource is
	def consume(self, res, loc):
		if res != None:
			for i in range(0, 2):
				if res.quantity != 0:
					for x in res.effects:
						if x[0]=="nutrition":
							self.nutrition+=x[1]
							if self.nutrition > 10:
								self.nutrition = 10
						if x[0]=="hydration":
							self.hydration+=x[1]
							if self.hydration > 10:
								self.hydration = 10
						if x[0]=="sleep":
							self.sleep+=x[1]
							if self.sleep > 10:
								self.sleep = 10
						if x[0]=="mind":
							self.entertain(x[1])

					if res.quantity != -1:
						res.quantity += -1

				else :
					loc.inventory.ressources.remove(res)
					break

		

	def o(self, nam):
		for x in self.inventory.tools:
			if x.name == nam:
				return x

		for x in self.inventory.entertainments:
			if x.name == nam:
				return x

		for x in self.inventory.ressources:
			if x.name == nam:
				return x

		#print("ERROR : can't select object, no object has this name")
		return None


	def talkToChatbot():
		return 0


	def talkToUser():
		return 0

	#mode : string
	def talk(self, person, c, mode="default"):
		self_idx = c.environment.characters.index(self)
		person_idx = c.environment.characters.index(person)

		if mode == "default" :
			#print random_conv or real_talk

			if r.randint(0,1) == 1 :
				self.relationships[person_idx] += 1;
				person.relationships[self_idx] += 1;
			else :
				self.relationships[person_idx] -= 1;
				person.relationships[self_idx] -= 1;

		else :
			#print cheerup
			value = r.randint(0,2)
			person.relationships[self_idx] += value;

		return 0


	#c : controller
	def act(self, c):
		f = open("output_hystory.txt", "a")

		#print(self.name)
		'''
		1 : update sleep hydration and nutrition
		2 : relationships passively wear out (not always)
		3 : search for food hydration and sleep
		4 : update mental state depending on f/h/s
		5 : act depending on their mental state and relationship with others
		6 : update mental state depending on the action taken
		'''

		#1
		if (self.hydration >= 1) & (self.nutrition >= 0.5) & (self.sleep >= 0.5):
			self.hydration+= -1
			self.nutrition+= -0.5
			self.sleep+= -0.5

			#2
			if (c.time % 10 == 0) & (c.time != 0):
				for value in self.relationships:
					value += -1

			#3
			bad = 0
			if self.hydrate(c) == False:
				bad += -1
			if self.eat(c) == False:
				bad += -1
			if self.sleeep(c) == False:
				bad += -1

			#4
			if bad < 0 :
				index = mind_enum.index(self.mind)
				if index != 0 :
					self.mind = mind_enum[index-1]

			#5 and 6
			self_idx = c.environment.characters.index(self)

			if self.mind == "depressed":
				dead = False
				if r.randint(0,5) == 0:
					for i in range(0,5):
						if (i != self_idx) & (self.relationships[i] == 0):
							c.environment.characters[i].alive = False
							#print("M U R D E R\n")
							self.mind = "apathetic"
							dead = True
							break

					for value in self.relationships:
						value += -3
						if value < 0:
							value = 0

					for people in c.environment.characters:
						people.relationships[self_idx] += -3
						if people.relationships[self_idx] < 0:
							people.relationships[self_idx] = 0

					if dead == False:
						self.alive = False
						#print("S U I C I D E\n")

				else:
					self.move(c.environment.rooms[self_idx+5]

			if self.mind == "apathetic":
				action = r.randint(1,3)
				if action == 1:
					liked = []
					for i in range(0,4):
						if (i != self_idx) & (self.relationships[i] >= 3):
							liked.append(c.environment.characters[i])
					if len(liked)-1 >= 0:
						self.talk(liked[r.randint(0,len(liked)-1)], c)


				else:
					books = ["Catcher_in_the_rye", "Millenium", "War_and_peace"]
					for book in books:
						for item in self.inventory.entertainments:
							if item.name == book:
								self.entertain(item.effect)
						for x in c.environment.rooms:
							if (x.state != "unusable") & (x.closed == False):
								if x.o(book) != None:
									self.take(x.o(book))
									self.entertain(x.o(book).effect)
									for i in range(5,10):
										if (x.name == c.environment.rooms[i]) & (self.relationships[i-5] < 5):
											self.relationships[i-5] += -1	
											for j in range(0,5):
												if c.environment.characters[j] == self:
													c.environment.characters[i-5].relationships[j] += -1
													break

			if self.mind == "neutral":
				person = r.randint(0,4)
				if c.environment.characters[person] != self:
					self.talk(c.environment.characters[person], c)
				else :
					person += 1
					if person == 5 :
						person = 0
					self.talk(c.environment.characters[person], c)

			if self.mind == "joyful":
				if r.randint(1,2) == 1:
					for person in c.environment.characters:
						if (person != self) & ((person.mind == "apathetic") | (person.mind == "depressed")):
							self.talk(person, c, "cheerup")
							break

				else :
					person = r.randint(0,4)
					if c.environment.characters[person] != self:
						self.talk(c.environment.characters[person], c)
					else :
						person += 1
						if person == 5 :
							person = 0
						self.talk(c.environment.characters[person], c)

			if self.mind == "determined":
				if self.nutrition != 10:
					self.eat(c)

				if r.randint(1,4) == 1:
					for i in range(0,5):
						if (i != self_idx) & (self.relationships[i] == 0):
							c.environment.characters[i].alive = False
							self.mind = "joyful"
							break

					for value in self.relationships:
						value += -3
						if value < 0:
							value = 0

					for people in c.environment.characters:
						people.relationships[self_idx] += -3
						if people.relationships[self_idx] < 0:
							people.relationships[self_idx] = 0

			else :
				liked = []
				for i in range(0,4):
					if (i != self_idx) & (self.relationships[i] >= 3):
						liked.append(c.environment.characters[i])
				if len(liked)-1 >= 0 :
					self.talk(liked[r.randint(0,len(liked)-1)], c)


			for value in self.relationships :
				if value < 0 :
					value = 0
				if value > 7 :
					value = 7

			self.move(c.environment.rooms[r.randint(0,9)])



		else:
			self.alive == False
			#print("D E A D\n")

		f.close()



	def hydrate(self, c):
		satisfied = False

		if self.o("water") != None:
			self.consume(self.o("water"), self)
			satisfied = True
		else:
			for x in c.environment.rooms:
				if (x.state != "unusable") & (x.closed == False):
					if x.o("water") != None:
						self.consume(x.o("water"), x)
						satisfied = True
						for i in range(5,10):
							if (x.name == c.environment.rooms[i]) & (self.relationships[i-5] < 5) & (self.relationships[i-5] > 0):
								self.relationships[i-5] += -1
								for j in range(0,5):
									if c.environment.characters[j] == self:
										c.environment.characters[i-5].relationships[j] += -1
										break

		return satisfied


	def eat(self,c):
		satisfied = False

		if self.mind == "apathetic":
			if r.randint(1,3) == 1:
				return satisfied


		foodtype = None
		if r.randint(0,4) == 0:
			foodtype = "good_food"
		else:
			foodtype == "food"


		if self.o(foodtype) != None:
			self.consume(self.o(foodtype), self)
			satisfied = True
		else:
			for x in c.environment.rooms:
				if (x.state != "unusable") & (x.closed == False):
					if x.o(foodtype) != None:
						self.consume(x.o(foodtype), x)
						satisfied = True
						for i in range(5,10):
							if (x.name == c.environment.rooms[i]) & (self.relationships[i-5] < 5) & (self.relationships[i-5] > 0):
								self.relationships[i-5] += -1
								self_idx = c.environment.characters.index(self)
								c.environment.characters[i-5].relationships[self_idx] += -1

		return satisfied


	def sleeep(self,c):
		satisfied = False

		if self.mind == "determined" :
			return satisfied

		for i in range(0,5):
			if c.environment.characters[i] == self:
				index = i
				break
		
		if (c.environment.rooms[index].closed == False) & (c.environment.rooms[index].state != "unusable"):
			self.sleep += 4
			satisfied = True

		else:
			for i in range(5,10):
				if (c.environment.rooms[index].closed == False) & (c.environment.rooms[index].state != "unusable"):
					self.sleep += 2

		return satisfied


class Room:
	def __init__(self, nam):
		self.name = nam
		self.inhabitants = [] #will be a list of Characters
		self.state = state_room_enum[1];
		self.closed = False
		self.inventory = Inventory()


	def o(self, nam):
		for x in self.inventory.tools:
			if x.name == nam:
				return x

		for x in self.inventory.entertainments:
			if x.name == nam:
				return x

		for x in self.inventory.ressources:
			if x.name == nam:
				return x

		#print("ERROR : can't select object, no object has this name")
		return None


class Tool :
	def __init__(self, n):
		self.name = n
		#quantitative attribute maybe?

class Ressource:
	def __init__(self, nam, eff, qua):
		self.name = nam
		self.effects = eff #sera un tableau de duplets
		self.quantity = qua

#nam : string / eff : int
class Entertainment:
	def __init__(self, nam, eff):
		self.name = nam
		self.effect = eff

class Inventory:
	def __init__(self):
		self.tools = [] #will be a list of Tool
		self.ressources = [] #will be a list of Ressource
		self.entertainments = [] #will be a list of Entertainement
