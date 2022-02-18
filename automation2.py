from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver')
driver.get("https://techwithtim.net")
time.sleep(7.5)

# time.sleep(5)

link = driver.find_element_by_link_text("Python Programming")
link.click()
time.sleep(2)

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     element.click()
	
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "sow-button-19310003"))
#     )
#     element.click()
	
# 					# while (driver.title != "Tech With Tim - Python & Java Programming Tutorials - techwithtim.net"):
# 					#     driver.back()
        
# except:
#     				# driver.quit() 

# 	time.sleep(1)
	
# driver.back()
# time.sleep(1)
# driver.back()
# time.sleep(1)
# driver.back()
# time.sleep(1)
driver.quit()