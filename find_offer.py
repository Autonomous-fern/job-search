import time  # nous permet de temporiser les requêtes à l'api dans une loop
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


PATH = "C:\Program Files (x86)\chromedriver.exe"  # indicate path to chromedriver
driver = webdriver.Chrome(PATH)  # select chrome driver

url1 = "https://www.seek.com.au/devops-jobs/in-All-Sydney-NSW?salaryrange=0-80000&salarytype=annual"
page = driver.get(url1)
