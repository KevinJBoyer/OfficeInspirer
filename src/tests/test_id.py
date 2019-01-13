import unittest

from models.id import Id



class TestId( unittest.TestCase ):

	def setUp(self):
		self.firstId = Id()
		self.secondId = Id()
		self.sameAsFirstId = firstId.copy()
		
		print self.firstId
		print self.secondId
		print self.sameAsFirstId


	def test_equal(self):
		self.assertEqual( self.firstId, self.sameAsFirstId )


	def test_notEqual(self):
		self.assertNotEqual( self.firstId, self.secondId )



if __name__ == '__main__':
    unittest.main()