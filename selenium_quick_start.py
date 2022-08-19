import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


PATH = "C:\Program Files (x86)\chromedriver.exe"  # indicate path to chromedriver
driver = webdriver.Chrome(PATH)  # select chrome driver


driver.get("https://www.google.com")  # open a webpage
# print(driver.title)  # --> return the weppage title
# time.sleep(2)


# to search a webpage element, right clic + inspect, then on python,
# seach by 1) ID, 2) name, 3) class
no_cookies = driver.find_element(By.ID, "W0wltc")  # click on "refuse all cookies"
no_cookies.click()

search = driver.find_element(By.NAME, "q")  # find search bar
search.send_keys('TEST')  # send input to search bar
search.send_keys(Keys.RETURN)  # simulate return key on search bar


time.sleep(1)
driver.quit()
