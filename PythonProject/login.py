import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://dev.hakini.net/login")

driver.fullscreen_window()
time.sleep(5)
#email_filed = driver.find_element(By.XPATH, "//form[@class='formsStyle float-right']/div[1]/div[1]/div[1]/input")
email_filed = driver.find_element(By.CSS_SELECTOR, "form[class='formsStyle float-right'] div:nth-of-type(1) div:nth-of-type(1) div:nth-of-type(1) input")
email_filed.send_keys("123")
time.sleep(10)