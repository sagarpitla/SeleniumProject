from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import  time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.spicejet.com/')
'''Move to Element'''
Login_link_ele = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
actionchains = ActionChains(driver)
actionchains.move_to_element(Login_link_ele).perform()

Speice_Link_ele = driver.find_element(By.LINK_TEXT,'SpiceClub Members')
actionchains.move_to_element(Speice_Link_ele).perform()

mem_login_ele = driver.find_element(By.LINK_TEXT,'Member Login')
mem_login_ele.click()
time.sleep(3)
driver.quit()
