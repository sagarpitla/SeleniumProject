from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import  time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
user=driver.find_element(By.ID, 'login1')
user.send_keys('sagar@mail.com')


