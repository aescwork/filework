"""

..	currentmodule:: filework
	:platform: Linux, Unix, Windows
	:synopsis: A simple wrapper class for easy reading (iterating) from, writing, and appending to files.

.. moduleauthor:: Vollund Leysing aescwork@protonmail.com


"""

import os


class FileWork(object):
	"""
		
	"""
	def __init__(self, file_path=None):
	
		"""
			
			Args:
				file_path: The name and optionally the path to the file.
		"""

		self.result = "NONE"
		self.status = "NONE"
		self.fd = None
		self._file_path = file_path		# This member is private because this class uses a property to get and set it.
		self.action = ""
		self._new_path = False

	def __del__(self):
		"""
		Make sure to close any open file descriptor when object is deleted.
		"""
		self.close_file()


	@property
	def file_path(self):
		"""
		Get the file path.
		"""
		return self._file_path


	@file_path.setter
	def file_path(self, val):
		"""
		This method is for assigning a value to self._file_path.  The self._file_path attribute can be accessed directly
		but the @property is used to call close_file() on the self.fd (the file descriptor).
		
		Args:
			val (str):	the path to the file for the object.
		"""
		
		try:
			self._file_path = val
			self.close_file()
			self._new_path = True
			self._set_result_and_status("OK", "")
		except Exception as e:
			self._set_result_and_status("FAIL", "In FileWork, file_path setter: ", str(e))
			

	def close_file(self):
		"""
		Close the file if there is a file descriptor.
		"""
		if self.fd:
			self.fd.close()
			self.fd = None


	def write_to_file(self, content):
		"""
			self._set_result_and_status("", "")
		
		"""
		if self._new_path:
			self._set_action("r")




	def append_to_file(self, content):
		"""
		"""
		
		if self._new_path or self.action != "a"):
			self._set_action("a") 

		try:
			if type(content) is list:
				for line in content:
					self.fd.write(content)	
			else:
				self.fd.write(content_str)
			self._set_result_and_status("OK", "")

		except Exception as e:
			self._set_result_and_status("FAIL", "In FileWork append_to_file(): " + str(e))



	def iterate_through_file(self):
		"""
				self._set_result_and_status("", "")
		"""
	

		if self._new_path:
			self._set_action("r")
			self._new_path = False




	def _set_action(self, new_action):

		self._new_path = False

		path = self.file_path
		if self.fd != "":
			self.fd.close()

		self.action = new_action
		self.file_path = path

		return self._file_open()



	def _file_open(self):
		"""
		Private method for the object to open the file in the correct way for the operation to be performed.
		"""
		ret_val = True
		try:			
			self.fd = open(self.file_path, self.action)
			self._set_result_and_status("OK", "")
		except Exception as e:
			self._set_result_and_status("FAIL", "in FileWork _file_open: " + str(e))
			ret_val = False
				
		return ret_val



	def _set_result_and_status(self, result, status):
		"""
		Set self.result and self.status here to help DRY out the code in the above methods.
		
		Args:
			result (string):	the result of the operation performed by the calling method.
			status (string):	the status (description) of the outcome of the operation performed by the calling method.
		"""
		self.result = result
		self.status = status

