# from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

# for the line below, where there is the "button" word, that is where you put the type / element

# print ("=======================================================")
# print ("=======================================================")
# print ("=======================================================")
# print ("=======================================================")
# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://techwithtim.net")

# print(driver.title)

# print ("===================================================================================================================")


driver = webdriver.Chrome('./chromedriver')
driver.get("https://techwithtim.net")

driver.quit
search = driver.find_element(By.CLASS_NAME,"search-field")

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        # header = article.find_element_by_link_text("HTTP Methods - GET & POST")
        print(header.text)
    # print(main.text)
finally:
    driver.quit()
# try catch block will wait x amount of time until 
# the element of the specified ID (or other element type) is located/identied before proceeding
# as opposed to setting a hard coded wait time and then looking for a particular id
# print(main.text)

# print ("===================================================================================================================")
# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://techwithtim.net")
# time.sleep(3.5)

# # time.sleep(5)

# link = driver.find_element_by_link_text("Python Programming")
# link.click()
# time.sleep(2)

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



# print ("===================================================================================================================")

# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://orteil.dashnet.org/cookieclicker/")

# driver.implicitly_wait(5) # this will wait and give everything time to load up

# cookie  = driver.find_element_by_id("bigCookie")
# cookie_count = driver.find_element_by_id("cookies")

# items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)] 

# 					# items = driver.find_element_by_id("productPrice1") 
# 					#[start, finish, increment/decrement] 
# 					# this will find productPrice1 & 0 but will loop to interate through them (1 -> 0)

# for i in range(50): 
# 	actions = ActionChains(driver) 
# 	actions.click(cookie) #this will click down on the mouse wherever the mouse is
# 	actions.perform()
# 	count = int(cookie_count.text.split(" ")[0])
# 	for item in items:
# 		value = int(item.text)
# 		if value <= count:
# 			upgrade_actions = ActionChains(driver)
# 			upgrade_actions.move_to_element(item)
# 			upgrade_actions.click()
# 			upgrade_actions.perform()
# 					# for i in range(5000):

# driver.quit() 

# continue from 11:43
