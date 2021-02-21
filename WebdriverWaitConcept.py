from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
from  selenium.webdriver.support.wait import WebDriverWait as wc
from selenium.webdriver.support import expected_conditions as ec
import  time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
wait=wc(driver,10)

user=wait.until(ec.presence_of_element_located((By.ID,'login1')))
user.send_keys('Sagar@mail.com')
driver.find_element(By.ID,'password').send_keys('Hello')
time.sleep(2)
driver.quit()