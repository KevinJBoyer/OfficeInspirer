import time
import unittest

from models.quote import Quote



class TestQuote( unittest.TestCase ):

	def setUp(self):
		self.newQuote = Quote( "Hello World!", "My Computer")


	def test_constructor(self):
		self.assertEqual( self.newQuote.say(), "Hello World! said My Computer" )


	def test_lastSaidIsUpdating(self):
		initLastSaid = self.newQuote.getLastSaid()

		time.sleep(0.01)

		self.newQuote.say()

		self.assertNotEqual( initLastSaid, self.newQuote.getLastSaid() )


	def test_lastSaidIsInPast(self):
		self.newQuote.say()

		time.sleep(0.01)

		self.assertTrue( self.newQuote.getLastSaid() < time.time() )



if __name__ == '__main__':
    unittest.main()
