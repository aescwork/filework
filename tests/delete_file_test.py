# -*- coding: utf-8 -*-

import unittest
import os 
import sys
sys.path.append("../filework/")
import filework as fw


class DeleteFromFileTest(unittest.TestCase):

	def setUp(self):

		self.path_to_write_file = "../fixtures/write_file.txt"
		self.f = fw.FileWork(self.path_to_write_file)  
		self.to_write = "Geri and Freki does Allfather Feed\nThe far-famed fighter of old\nBut on wine alone\nDoes the weapon-decked God\nOdhinn, forever live\n"

		self.f.write_to_file(self.to_write)


	def test_delete_file(self):
		"""
		Test the results of deleting a file.  
		"""

		self.f.delete_file()

		self.assertEqual(os.path.isfile(self.path_to_write_file), False)
		self.assertEqual(self.f.result, "OK")


	def tearDown(self):

		self.f.__del__()


if __name__ == '__main__':
	unittest.main()





