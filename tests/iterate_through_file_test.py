# -*- coding: utf-8 -*-

import unittest
import shutil
import sys
sys.path.append("../filework/")
import filework as fw


class IterateThroughFileTest(unittest.TestCase):

	def setUp(self):

		self.path_to_write_file = "../fixtures/write_file.txt"
		self.wrong_path = "../filework/write_file.txt"
		self.f = fw.FileWork(self.path_to_write_file)  
		
		self.to_write = "Geri and Freki does Allfather Feed\nThe far-famed fighter of old\nBut on wine alone\nDoes the weapon-decked God\nOdhinn, forever live\n"
		self.matter_list = ['Geri and Freki does Allfather Feed\n', 'The far-famed fighter of old\n', 'But on wine alone\n', 'Does the weapon-decked God\n', \
						'Odhinn, forever live\n', 'EOF']

		self.f.write_to_file(self.to_write)


	def test_iterate_through_file(self):
		"""
		Test the values returned by iterate_through_file in the first loop. In the second loop, test the "s" argument
		to iterate_through_file and confirm that the file is closed.  The third loop attempts to create an error condition
		to test the output of iterate_through_file when something goes wrong.
				
		"""

		for i in range(0,6):
			self.assertEqual(self.f.iterate_through_file("n"), self.matter_list[i])	

		for i in range(0,6):
			if i == 4:
				self.f.iterate_through_file("s")
				self.assertEqual(self.f.is_file_open, False)
				break
		
		for i in range(0,6):
			if i == 4:
				shutil.move(self.path_to_write_file, self.wrong_path)
				self.assertEqual(self.f.iterate_through_file("n"), "ERR")
				shutil.move(self.wrong_path, self.path_to_write_file)
				break
			else:
				self.f.iterate_through_file("n")

	def test_result(self):
		self.assertEqual(self.f.result, "OK")


	def tearDown(self):

		self.f.__del__()


if __name__ == '__main__':
	unittest.main()





