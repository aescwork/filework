# -*- coding: utf-8 -*-

import unittest
import os
import sys
sys.path.append("../filework/")
import filework as fwk


class FilePathSetter(unittest.TestCase):
	
	"""
	Test that all of the code in the @file_path.setter method is executed.
	"""

	def setUp(self):
		self.fw = fwk.FileWork()  
		self.test_path = "/home/user/a/path/to/his/file"
		self.fw.file_path = self.test_path

	def test_file_path(self):

		self.assertEqual(self.fw.file_path, self.test_path)	


	def test_result(self):
		self.assertEqual(self.fw.result, "OK")
		self.assertEqual(self.fw.status, "set new file_path")
		self.assertEqual(self.fw.new_path, True)
		self.assertEqual(self.fw.fd, None)


	def tearDown(self):

		self.fw.__del__()


if __name__ == '__main__':
	unittest.main()
