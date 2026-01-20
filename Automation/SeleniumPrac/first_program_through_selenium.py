import time

from selenium import webdriver


# Webdriver communicate with browser
driver= webdriver.Chrome()

# driver send request to browser through URL
driver.get("https://www.facebook.com/")

time.sleep(5)

driver.quit()