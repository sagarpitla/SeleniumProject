from selenium import  webdriver
from selenium.webdriver.common.by import  By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import  time

broswerName = "chrome"

if broswerName == "chrome":
  driver= webdriver.Chrome(ChromeDriverManager.install())
elif broswerName == "firefox":
    driver = webdriver.firefox(executable_path=GeckoDriverManager.install())
else:
    print('Please select required broswer'+broswerName)