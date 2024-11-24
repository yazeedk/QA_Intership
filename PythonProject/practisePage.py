import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.ID, "username").send_keys("kmail.solaf@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("12345678")
driver.find_element(By.XPATH, "//div[@class='form-group']/label/span/input").click()
#CSS SELECTOR : "div[class='form-group'] label span input"
driver.find_element(By.CLASS_NAME, "btn-info").click()

#wait = WebDriverWait(driver, 10)
#wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

alert_message = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text

assert alert_message == "Incorrect username/password."



time.sleep(3)