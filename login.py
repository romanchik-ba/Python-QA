    ## !!! CHECK README.MD BEFORE EXECUTING THE TEST !!!
# Import necessary libraries
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys

options = Options()
options.page_load_strategy = "eager"
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")

# Set up ChromeDriver and launch Chrome browser.
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Locators
account = ("xpath", "/html/body/header/div[3]/div/div/div/div/a[1]")
create = ("xpath", "//*[@id='login-form']/div[5]/a")
login = ("xpath", "//*[@id='loginform-username']")
passwd = ("xpath", "//*[@id='loginform-password']")
log_btn = ("xpath", "//*[@id='login-form']/div[6]/button")

driver.get("https://tritonshoes.ru")

# Clicking on account button
driver.find_element(*account).click()
time.sleep(2)

# Login, e-mail and password input in fields
driver.find_element(*login).send_keys("login_not_taken_yet_i_hope")
time.sleep(2)
driver.find_element(*passwd).send_keys("123password123")
time.sleep(2)
driver.find_element(*log_btn).click()
time.sleep(5)