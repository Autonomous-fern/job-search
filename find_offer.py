import time  # nous permet de temporiser les requêtes à l'api dans une loop
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


PATH = "C:\Program Files (x86)\chromedriver.exe"  # indicate path to chromedriver
driver = webdriver.Chrome(PATH)  # select chrome driver

url1 = "https://www.seek.com.au/devops-jobs/in-All-Sydney-NSW?salaryrange=0-80000&salarytype=annual"
page = driver.get(url1)
time.sleep(3)

announce_titles_elements = driver.find_elements(By.XPATH, "//a[@data-automation= 'jobTitle']")
announce_titles = [element.text for element in announce_titles_elements]

announce_company_elements = driver.find_elements(By.XPATH, "//a[@data-automation= 'jobCompany']")
announce_companies = [element.text for element in announce_company_elements]

announce_location_elements = driver.find_elements(By.XPATH, "//a[@data-automation= 'jobLocation']")
announce_locations = [element.text for element in announce_location_elements]


print(announce_locations)


# need to separate functions : open chrome, find job titles on the open chrome window
