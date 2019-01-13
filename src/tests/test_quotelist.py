import logging
import unittest
import time

from models.quote import Quote
from models.quotelist import QuoteList


logging.basicConfig(level=logging.DEBUG)


class TestQuoteList( unittest.TestCase ):

	def setUp(self):
		self.quotelist = QuoteList()
		self.quotelist.add( Quote("Hi", "Me") )


	def test_add(self):
		self.assertEqual( len(self.quotelist.quotes),  1 )


	def test_addSameId(self):
		newQuote = self.quotelist.quotes[0].copy()

		self.assertEqual( \
				self.quotelist.quotes[0].id, \
				newQuote.id \
			)

		self.quotelist.add( newQuote )

		self.assertEqual( len(self.quotelist.quotes), 2 )

		self.assertNotEqual( \
				self.quotelist.quotes[0].id, \
				self.quotelist.quotes[1].id \
			)


	def test_getRandomChoice(self):
		self.assertEqual( \
				self.quotelist.getRandomQuote().say(), \
				"Hi said Me" \
			)


	def test_delete(self):
		self.quotelist.delete("this id can't be in the list")
		self.assertEqual( len(self.quotelist.quotes),  1 )

		self.quotelist.delete( self.quotelist.quotes[0].id )
		self.assertEqual( len(self.quotelist.quotes),  0 )


	def test_getLastSaid(self):
		self.assertEqual( \
			self.quotelist.quotes[0], \
			self.quotelist.getLastSaid() \
			)

		# Any time we add a new quote, it should be the most recently said
		time.sleep(0.01)
		self.quotelist.add( Quote("Hello again", "Someone else") )
		self.assertEqual( \
			self.quotelist.quotes[1], \
			self.quotelist.getLastSaid() \
			)

		self.quotelist.quotes[0].say()
		self.assertEqual( \
			self.quotelist.quotes[0], \
			self.quotelist.getLastSaid() \
			)



if __name__ == '__main__':
    unittest.main()