# -*- coding: utf-8 -*-

import unittest
import os
import sys
sys.path.append("../filework/")
import filework as fw


class AppendToFileTest(unittest.TestCase):

	def setUp(self):
		self.f = fw.FileWork()  

		path_to_append_file = "../fixtures/write_file.txt"
		self.matter_to_write = "Geri and Freki does Allfather Feed\nThe far-famed fighter of old\nBut on wine alone\nDoes the weapon-decked God\nOdhinn, forever live"
		self.matter_to_append = "\nHuginn and Munnin every day\nOver Jormungrund fly" 
		self.comp = self.matter_to_write + self.matter_to_append

		self.f = fw.FileWork(path_to_append_file)
		self.f.write_to_file(self.matter_to_write)
		self.f.append_to_file(self.matter_to_append, True)	# method call: pass True to make sure file closes after the operation so the file can be read
															# properly for the test.
		self.result = self.f.result							

		self.fd = open(path_to_append_file, "r")
		self.write_file_content = self.fd.read()
		
			

	def test_append_to_file(self):

		self.assertEqual(self.comp, self.write_file_content)	

	def test_result(self):
		self.assertEqual(self.f.result, "OK")


	def tearDown(self):

		self.fd.close()		
		self.f.close_file()
		self.f.__del__()


if __name__ == '__main__':
	unittest.main()





