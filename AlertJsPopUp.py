from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import  time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.NAME,'proceed').click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#alert.dismiss()
#alert.send_keys('')
driver.switch_to.default_content()
#Type='file' is required to normally use sendkeys 
