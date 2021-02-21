from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import  time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')

source = driver.find_element(By.ID, 'draggable')
Target = driver.find_element(By.ID, 'droppable')
actionschain = ActionChains(driver)
#actionschain.drag_and_drop(source,Target).perform()
'''actionschain.\
    click_and_hold(source).\
    move_to_element(Target).\
    release().\
    perform()'''




