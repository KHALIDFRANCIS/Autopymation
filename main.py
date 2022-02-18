from email.iterators import typed_subpart_iterator
import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):  #we inherit from unittest.testcase to incorporate things that will be used
	
	def setUp(self):  #this has all thats needed for testing setup....this will be the opener
		print("setup")
		self.driver = webdriver.Chrome('./chromedriver')
		self.driver.get("http://www.python.org")

	def test_exp1(self):	#test case method MUST BEGIN WITH "test"...anything else wont work
		print("Test1")
		assert True   
		#if argument on right side of "assert" is true, then test passes and it prints "OK". If false, then test fails and it prints "FAILED"

	def test_exp2(self):
		print("Test#2")
		# assert False
		assert True

	def test_exp3(self):
		print("TEST NUMBA 3")
		assert False
		# assert True

	def test_exp4(self):
		print("TEST NUMBA 4")
		assert True

	def test_exp5(self):
		print("TEST NUMBA 5")
		assert False
		# assert True

	def not_a_test(self):
		print("this wont print")

	def teardown(self): #this will be the closer
		print("teardown")
		self.driver.close()
	
if __name__=="__main__":
	unittest.main()	#this will run all the unit tests that we will define / create / wrote
					#since everything falls under unittest, they are all classified as defined


# the testing execution pattern will go as follows
# setup => test_exp1 => teardown
# setup => test_exp2 => teardown
# setup => test_exp3 => teardown
# so setup AND TEARDOWN WILL RUN EVERY SINGLE TIME
		 


# continue from  10:25