from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, DesiredCapabilities
from  selenium.webdriver.support.wait import WebDriverWait as wc
from selenium.webdriver.support import expected_conditions as ec
import  time

# options= Options()
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('--ignore-certificate-errors')
# desired_capablities = DesiredCapabilities().CHROME.copy()
# desired_capablities['acceptInsecureCerts']= True
options= Options()
options.set_capability('acceptInsecureCerts',True)
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)



driver.get('https://expired.badssl.com/')
time.sleep(4)
driver.quit()