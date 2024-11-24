import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.hakini.net/signup")


driver.maximize_window()

frame = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(frame)
driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()
print("Solve Recaptcha")
input("Waiting...!")
time.sleep(5)
