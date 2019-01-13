import random



class Id:

	# 100 most common nouns in English
	USABLE_WORDS = ["woman", "life", "child", "world", "school", "state",
		 "family", "student", "group", "country", "problem",
		 "hand", "part", "place", "case", "week", "company",
		 "system", "program", "question", "work", "government",
		 "number", "night", "point", "home", "water", "room",
		 "mother", "area", "money", "story", "fact", "month",
		 "lot", "right", "study", "book", "eye", "job", "word",
		 "business", "issue", "side", "kind", "head", "house",
		 "service", "friend", "father", "power", "hour", "game",
		 "line", "end", "member", "law", "car", "city", "community",
		 "name", "president", "team", "minute", "idea", "kid",
		 "body", "information", "back", "parent", "face", "others",
		 "level", "office", "door", "health", "person", "art",
		 "war", "history", "party", "result", "change", "morning",
		 "reason", "research", "girl", "guy", "moment", "air",
		 "teacher", "force", "education"]


	def __init__( self, identifier = False, idLength = 3, separator = " " ):

		if not identifier:
			randomWords = [ random.choice( self.USABLE_WORDS ) for i in range( idLength ) ]
			self.identifier = separator.join( randomWords )
		else:
			self.identifier = identifier


	def __repr__( self ):
		return self.identifier


	def __eq__( self, other ):
		return self.__repr__() == other.__repr__()


	def __ne__( self, other ):
		return not self.__eq__( other )


	def copy(self):
		copy = Id()
		copy.identifier = self.identifier
		return copy