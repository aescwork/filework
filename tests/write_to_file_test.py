# -*- coding: utf-8 -*-

import unittest
import os
import sys
sys.path.append("../filework/")
import filework as fw


class WriteToFileTest(unittest.TestCase):

	def setUp(self):
		path_to_write_file = "../fixtures/write_file.txt"
		self.matter_to_write = "Geri and Freki does Allfather Feed\nThe far-famed fighter of old\nBut on wine alone\nDoes the weapon-decked God\nOdhinn, forever live"
		
		self.f = fw.FileWork(path_to_write_file)
		self.f.write_to_file(self.matter_to_write)
		self.result = self.f.result
	
		self.f.close_file()

		self.fd = open(path_to_write_file, "r")
		self.comp = self.fd.read()

	def test_write_to_file(self):

		self.assertEqual(self.matter_to_write, self.comp)	


	def test_result(self):
		self.assertEqual(self.f.result, "OK")


	def tearDown(self):

		self.fd.close()		
		self.f.__del__()


if __name__ == '__main__':
	unittest.main()
