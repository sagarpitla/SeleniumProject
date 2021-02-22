from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
from  selenium.webdriver.support.wait import WebDriverWait as wc
from selenium.webdriver.support import expected_conditions as ec
import  time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(4)
driver.get('http://classic.crmpro.com/')
#Mobile_Link=driver.find_element(By.LINK_TEXT,'Mobiles')
# driver.execute_script("arguments[0].click();",Mobile_Link)
#
# title= driver.execute_script("return document.title;")
# print(title)
#driver.execute_script("history.go(0);")
#driver.execute_script("alert('Welcome to automation')")
#driver.execute_script("arguments[0].style.border = '3px solid blue'",Mobile_Link)

print_sms=driver.find_element(By.XPATH,"//h3[contains(text(),'Print & SMS')]")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script("arguments[0].scrollIntoView(true);",print_sms)
time.sleep(5)
driver.quit()