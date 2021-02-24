from time import sleep
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(2)
driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys("yourusername")
driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys("yourpassword")
driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()
sleep(3)
driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
    .click()
driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
    .click()
sleep(5)


