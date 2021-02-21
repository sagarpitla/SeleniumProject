from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\User\\Desktop\\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
driver.quit()


