# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("../filework/")
import filework as fw


class SomeTest(unittest.TestCase):

	def setUp(self):

		self.path_to_write_file = "../fixtures/write_file.txt"
		self.wrong_path = "../filework/write_file.txt"
		self.f = fw.FileWork(self.path_to_write_file)  
		self.fe = fw.FileWork(self.wrong_path)  
		self.to_write = "Geri and Freki does Allfather Feed\nThe far-famed fighter of old\nBut on wine alone\nDoes the weapon-decked God\nOdhinn, forever live\n"


		self.f.write_to_file(self.to_write)


	def test_read_from_file(self):
		"""
		Test the results of reading from a file.  Then test the results of an attempted read from a non-existent file (error condition: wrong location).
		"""

		self.contents = self.f.read_from_file()
		self.err_contents = self.fe.read_from_file()

		self.assertEqual(self.contents, self.to_write)
		self.assertEqual(self.err_contents, "ERR")


	def tearDown(self):

		self.f.__del__()


if __name__ == '__main__':
	unittest.main()





