from selenium import webdriver
from selenium.webdriver.common.by import  By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

def select_values(element,values):
    select = Select(element)
    select.select_by_visible_text(values)

ele_indus = driver.find_element(By.ID, 'Form_submitForm_Industry')
ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
select_values(ele_country,'Afghanistan')
#select_values(ele_indus,'Aerospace')

select = Select(ele_indus)
indus_list = select.options

for ele in indus_list:
    print(ele.text)
    if ele.text == 'Automotive':
        ele.click()
        break

