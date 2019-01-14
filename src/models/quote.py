import time


from models.id import Id



class Quote:


	def __init__( self, theSaying, author, id = False, lastSaid = False ):
		if not id: id = Id()
		if not lastSaid: lastSaid = time.time()

		self.theSaying = theSaying
		self.author = author
		self.id = id
		self.lastSaid = lastSaid


	def __repr__(self):
		return 'Quote `%s`: "%s" - %s. Last said %s.' % \
			(self.id, self.theSaying, self.author, self.lastSaid)


	def __eq__( self, other ):
		return self.id == other.id


	def __ne__( self, other ):
		return not self.__eq__(other)


	def __lt__( self, other ):
		return self.lastSaid < other.lastSaid


	def __gt__( self, other ):
		return self.lastSaid > other.lastSaid


	def say(self):
		self.lastSaid = time.time()
		return "%s said by %s" % (self.theSaying, self.author)


	def getLastSaid(self):
		return self.lastSaid


	def getId(self):
		return self.id


	# returns exact copy, including ID
	def copy( self ):
		return Quote( self.theSaying, self.author, self.id.copy(), self.lastSaid )


	# returns partial copy with new ID
	def copyWithNewId( self ):
		return Quote( self.theSaying, self.author, Id(), self.lastSaid )
