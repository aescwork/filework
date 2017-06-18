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
		self.new_path = False


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
		but the @property is used to call setter method.

		When a new value is assigned to _file_path, close_file() is called on the fd (the file descriptor) if a file was
		actually assigned to it.  Next, new_path is is set to True, meaning that the object is working with a new file.
		This will make sure that the methods which do the actual work with the files open the new file properly -- either to
		'a' (append), 'w' (write) or 'r' (read) the file.  

		Args:
			val (str):	the path to the file for the object.
		"""
		
		try:
			self._file_path = val
			self.close_file()
			self.new_path = True
			self._set_result_and_status("OK", "set new file_path")
		except Exception as e:
			self._set_result_and_status("FAIL", "In FileWork, file_path setter: ", str(e))
			

	def close_file(self):
		"""
		Close the file if there is a file descriptor.  This method is called automatically by @file_path.setter 
		if the value of self._file_path is changed.
		"""
		if self.fd:
			self.fd.close()
			self.fd = None


	def write_to_file(self, content):
		"""
		This method will write all of 'content' to the file.  The file is opened with the "w" mode: therefore if the file does not exist
		it will attempt to create it.  If the file exists already anything in the file will be deleted.  If content is None and the file does
		not exist, the only action will be that the file is created.
		
		Calls self._to_file to do the actual work.

		Args:
			content (str), (list), (NoneType):	
											The matter to be written to the file or a value of None which will only result in the file being
											created if it does not exist.

		
		"""

		self._to_file("w", "write_to_file", content)



	def append_to_file(self, content):
		"""
		Append to a file. 

		Calls self._to_file to do the actual work.

		Args:
				content (str), (list):	the matter to append to the file.
		"""
		
		self._to_file("a", "append_to_file", content)



	def iterate_through_file(self, move):
		"""
		Read a file by iterating or stepping through it one line at a time.

		Args:
		
			move (str):		what action to take with this method call: values are "n" for go to the next line, or "s" to stop iterating
							through the file, close the file descriptor, etc.

		Returns:
					(str) The current line of the file which has just been read, "EOF" which means the end of the file has been reached,
							or "ERR" which means something else went wrong..
							
		"""
	
		ret = ""
		if self.new_path or self.action != "r":
			self._set_action("r")
			
		if self.is_file_open:
			if move == "n":
				try:
					ret = next(self.fd)
				except StopIteration:
					ret = "EOF"
					self.fd.close()
					self._set_result_and_status("OK", "")
				except Exception as e:
					ret = "ERR"
					self._set_result_and_status("FAIL", "In FileWork, iterate_through_file(): " + str(e))
					self.fd.close()

			elif move == "s":
				self._set_result_and_status("OK", "")
				self.fd.close()
				
				
		return ret

	def read_from_file(self):
		"""
		Read and return the entire contents of the file of this object.

		Args:
				none	

		Returns:
					(?) The entire contents of a file.
							
		"""
	

		ret = ""

		if self.new_path or self.action != "r":
			self._set_action("r")


		try:
			ret = self.fd.read()
			self._set_result_and_status("OK", "")
		except Exception as e:
			self._set_result_and_status("FAIL", "In FileWork, read_from_file(): ", str(e))

		return ret


	def _set_action(self, new_action):

		self.new_path = False

		path = self.file_path
		if self.fd is not None:
			self.fd.close()

		self.action = new_action
		self.file_path = path

		return self._file_open()



	def _file_open(self):
		"""
		Private method for the object to open the file in the correct way for the operation to be performed.
		"""
		self.is_file_open = True
		try:			
			self.fd = open(self.file_path, self.action)
			self._set_result_and_status("OK", "")
		except Exception as e:
			self._set_result_and_status("FAIL", "in FileWork _file_open: " + str(e))
			self.is_file_open = False
				

	def _to_file(self, action, f_name, content):

		"""
		Private method for either writing or appending content to a file.

		Args:
				action (str):	"w", "a", "r" (The mode in which the file is to be opened).
				f_name (str):	The name of the "public facing" function which calls this method (for the message in teh status member).
				content (str), (list) (NoneType):	the matter to append to the file.
		"""

		if self.new_path or self.action != action:
			self._set_action(action) 

		if type(content) is list:
			content = "".join(content)

		if content and self.is_file_open:
			try:
				self.fd.write(content)
				self._set_result_and_status("OK", "")
			except Exception as e:
				msg = "In Filework " + f_name + "(): " + str(e)
				self._set_result_and_status("FAIL", msg)


	def _set_result_and_status(self, result, status):
		"""
		Set self.result and self.status here to help DRY out the code in the above methods.
		
		Args:
			result (string):	the result of the operation performed by the calling method.
			status (string):	the status (description) of the outcome of the operation performed by the calling method.
		"""
		self.result = result
		self.status = status

