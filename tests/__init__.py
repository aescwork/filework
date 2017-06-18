import sys
import unittest
sys.path.append("../filework/")
import filework as fw


class InstantiationTest(unittest.TestCase):

	def setUp(self):
		self.fwk = fw.FileWork("test.db")


	def testMemberResult(self):
		self.assertEqual(self.fwk.result, "NONE")
			

	def testMemberStatus(self):
		self.assertEqual(self.fwk.status, "NONE")

	
	def tearDown(self):
		self.fwk.__del__()

if __name__ == '__main__':
	unittest.main()
