from lib2to3.pgen2 import driver


class BasePage(object):
	def __init__(self, driver):		#this is the constructor method and will be inherited 
		self.driver = driver

class MainPage(BasePage): 		#this will inherit from BasePage
	def is_title_matches(self):
		return "Python" in self.driver.title


		# continue from 14:01