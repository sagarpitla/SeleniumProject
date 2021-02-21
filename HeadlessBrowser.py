from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import  time

options= webdriver.ChromeOptions()
#options.headless= False
options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get('https://www.amazon.in/')
print(driver.title)
