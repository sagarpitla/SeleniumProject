from selenium import webdriver
from selenium.webdriver.common.by import  By
from webdriver_manager.chrome import ChromeDriverManager

import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
linkList = driver.find_elements(By.TAG_NAME, 'a')
print(len(linkList))
for ele in linkList:
    linktext = ele.text
    print(linktext)
    print(ele.get_attribute('href'))

imageList = driver.find_elements(By.TAG_NAME, 'img')
print(imageList)

for ele in imageList:
    print(ele.get_attribute('src'))
