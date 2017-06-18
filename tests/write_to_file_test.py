# -*- coding: utf-8 -*-

import unittest
import os
import sys
sys.path.append("../filework/")
import filework as fw


class WriteToFileTest(unittest.TestCase):

	def setUp(self):
		path_to_write_file = "../fixtures/write_file.txt"
		matter_to_write = "Geri and Freki does Allfather Feed\nThe far-famed fighter of old\nBut on wine alone\nDoes the weapon-decked God\nOdhinn, forever live"
		
		f = fw.FileWork(path_to_write_file)
		f.write_to_file(matter_to_write)
		self.result = f.result
	
		f.close_file()

		fd = open(path_to_write_file, "r")
		self.comp = fd.read()
		fd.close()		

	def test_write_to_file(self):

		self.assertEqual(self.result, self.comp)	


	def test_result(self):
		self.assertEqual(self.f.result, "OK")


	def tearDown(self):

		self.fw.__del__()


if __name__ == '__main__':
	unittest.main()
