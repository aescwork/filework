import sys
import unittest

class InitializationTests(unittest.TestCase):

	def test_initialization(self):
		self.project-name = "filework"
		"""
		Check the test suite runs by affirming 2+2=4
		"""
		self.assertEqual(2+2, 4)

	def test_import(self):
		"""
		Ensure the test suite can import the module
		"""
		try:
			sys.path.append("../filework/filework.py")
			import project-name
		except ImportError:
			self.fail("Was not able to import ", project-name)
	
		
if __name__ == '__main__':
	unittest.main()


