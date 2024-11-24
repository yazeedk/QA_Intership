import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
# Class name -> blinkingText
# CSS SELECTOR

#switch to the next page
windows = driver.window_handles
driver.switch_to.window(windows[1])

email = driver.find_element(By.CSS_SELECTOR, "strong a").text

driver.switch_to.window(windows[0])
driver.find_element(By.ID, "username").send_keys(email)

time.sleep(5)