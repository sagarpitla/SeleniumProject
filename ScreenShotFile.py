from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import  time

options=webdriver.ChromeOptions()
options.headless= True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://www.reddit.com/')
#driver.get_screenshot_as_file('Amazon.png')
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_full.png')
