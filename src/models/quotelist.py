import random

from models.quote import Quote
from models.id import Id



class QuoteList:

	def __init__( self ):
		self.quotes = []


	def add( self, newQuote ):

		while newQuote in self.quotes:
			newQuote = newQuote.copyWithNewId()

		self.quotes.append(newQuote)


	def getRandomQuote( self ):
		return random.choice( self.quotes )


	def delete( self, quoteId ):
		bogey = Quote( "", "", quoteId )

		try:    self.quotes.remove(bogey)
		except: pass


	def getLastSaid( self ):
  		return max(self.quotes)
