from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import  time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.in/')
driver.find_element(By.LINK_TEXT,'Mobiles').click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.back()
driver.quit()
