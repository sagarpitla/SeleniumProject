import xlrd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import  time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

url= driver.find_element(By.ID,'Form_submitForm_subdomain')
firstname = driver.find_element(By.ID,'Form_submitForm_FirstName')
lastname = driver.find_element(By.ID,'Form_submitForm_LastName')
emailid= driver.find_element(By.ID,'Form_submitForm_Email')
jobtitle= driver.find_element(By.ID,'Form_submitForm_JobTitle')
company= driver.find_element(By.ID,'Form_submitForm_CompanyName')
phone= driver.find_element(By.ID,'Form_submitForm_Contact')
totalemp= driver.find_element(By.ID,'Form_submitForm_NoOfEmployees')
industry= driver.find_element(By.ID,'Form_submitForm_Industry')
country= driver.find_element(By.ID,'Form_submitForm_Country')





workbook= xlrd.open_workbook('file_example_XLS_10.xls')


#get total row count
sheet= workbook.sheet_by_name("registration")
rowcount = sheet.nrows
colnum = sheet.ncols
print("Total row count",rowcount,"Total col count",colnum)
for row_con in range(1, rowcount):
    url_= sheet.cell_value(row_con,0)
    first_name = sheet.cell_value(row_con,1)
    last_name = sheet.cell_value(row_con, 2)
    email_id = sheet.cell_value(row_con, 3)
    job_title = sheet.cell_value(row_con, 4)
    company_ = sheet.cell_value(row_con, 5)
    phone_ = sheet.cell_value(row_con, 6)
    total_emp = sheet.cell_value(row_con, 7)
    industry_ = sheet.cell_value(row_con, 8)
    country_ = sheet.cell_value(row_con, 9)

    url.clear()
    url.send_keys(url_)
    firstname.clear()
    firstname.send_keys(first_name)
    lastname.clear()
    lastname.send_keys(last_name)
    emailid.clear()
    emailid.send_keys(email_id)
    jobtitle.clear()
    jobtitle.send_keys(job_title)
    phone.clear()
    phone.send_keys(phone_)
    country.send_keys(country_)

driver.quit()
