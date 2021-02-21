from selenium import webdriver
from selenium.webdriver.common.by import  By
from webdriver_manager.chrome import ChromeDriverManager

import time
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)
username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
feature = driver.find_element(By.ID, 'Features')
username_url.send_keys("Hello")
first_name.send_keys("NaveenAutomation")
last_name.send_keys("Automation Labs")
email.send_keys("sagar@mail.com")
feature.click()
driver.quit()
