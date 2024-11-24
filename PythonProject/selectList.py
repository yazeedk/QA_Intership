import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.hakini.net/signup")


driver.maximize_window()

# Locate the dropdown by ID
dropdown = Select(driver.find_element(By.ID, "searchList"))

# Select an option by visible text
dropdown.select_by_visible_text("Afghanistan (+93)")

time.sleep(5)
