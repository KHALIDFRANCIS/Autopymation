from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver')
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5) # this will wait and give everything time to load up

cookie  = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)] 

					# items = driver.find_element_by_id("productPrice1") 
					#[start, finish, increment/decrement] 
					# this will find productPrice1 & 0 but will loop to interate through them (1 -> 0)

for i in range(50): 
	actions = ActionChains(driver) 
	actions.click(cookie) #this will click down on the mouse wherever the mouse is
	actions.perform()
	count = int(cookie_count.text.split(" ")[0])
	for item in items:
		value = int(item.text)
		if value <= count:
			upgrade_actions = ActionChains(driver)
			upgrade_actions.move_to_element(item)
			upgrade_actions.click()
			upgrade_actions.perform()
					# for i in range(5000):

driver.quit() 

# continue from 11:43
