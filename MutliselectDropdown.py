from selenium import webdriver
from selenium.webdriver.common.by import  By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

def select_values(optionslist, value):
    if not value[0] == 'all':
        for ele in droplist:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in optionslist:
                ele.click()
        except Exception as e:
            print(e)



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)
driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(2)
droplist = driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
value_list = ['choice 2','choice 3','choice 6 2 1']
#value_list = ['choice 7']
#value_list = ['all']

select_values(droplist,value_list)
driver.quit()