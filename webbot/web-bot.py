from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#you can also use Chrome instead of Firefox
driver = webdriver.Firefox()
#Url
driver.get("http://www.facebok.com")
#finding elements by inspecting and input
email = driver.find_element(By.ID, "email")
email.send_keys("test")
passw = driver.find_element(By.ID, "pass")
passw.send_keys("test")
btn=driver.find_element(By.NAME, "login")
btn.click()
#print
print('added')
#sleep for some time
time.sleep(10)
#exit
driver.close()
