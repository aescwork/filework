# -*- coding: utf-8 -*-

import unittest
import os
import sys


class ASampleTest(unittest.TestCase):

	def setUp(self):
		self.obj = scf.SomeClass()  


	def test_some_method(self):

		self.assertEqual(someval, compval)	

	def test_result(self):
		self.assertEqual(self.obj.result, "OK")


	def tearDown(self):

		self.obj.__del__()


if __name__ == '__main__':
	unittest.main()
