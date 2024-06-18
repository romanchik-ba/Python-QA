    ## !!! CHECK README.MD BEFORE EXECUTING THE TEST !!!
# Import necessary libraries
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(options = options)

# Set up ChromeDriver and launch Chrome browser.
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 18, poll_frequency=1)

# Locators
men_shoes = ("xpath", "/html/body/header/div[3]/div/div/div/nav/ul/li[2]/a")
boots = ("xpath", "/html/body/div[1]/section/div/div[2]/div/div[2]/div[1]/div/div/a[2]")
corz_fb = ("xpath", "//*[@id='w0']/div[1]/div[1]/div[4]/a[2]")
cart = ("xpath", "//a[@id='miniCart']")
buy = ("xpath", "//*[@id='tov_pop3573']/section/div[2]/a[1]")
close_btn = ("xpath", "//*[@id='tov_pop3573']/button")
order_reg = ("xpath", "/html/body/div[1]/section/div/div[2]/div/div/div/a[2]")
log_field = ("xpath", "//*[@id='signupform-username']")
email = ("xpath", "//*[@id='signupform-email']")
passwd = ("xpath", "//*[@id='signupform-password']")
submit = ("xpath", "//*[@id='form-signup']/div[4]/button")
success_order_line = ("xpath", "/html/body/div[1]/section/div/div[2]/div")

driver.get("https://tritonshoes.ru")

### Test Case ' '
# Click on the Men Shoes button
driver.find_element(*men_shoes).click()
time.sleep(2)

# Clicking on item "Ботинки"
driver.find_element(*boots).click()
time.sleep(2)

# Clicking on cart button
driver.find_element(*corz_fb).click()
time.sleep(5)

# Clicking on buy button
wait.until(EC.element_to_be_clickable(buy)).click()
time.sleep(3)

# Clicking on close button
driver.find_element(*close_btn).click()
time.sleep(4)

# Clicking on cart button
driver.find_element(*cart).click()
time.sleep(2)

# Clicking on "Order with registration" button
driver.find_element(*order_reg).click()
time.sleep(2)

# Login, e-mail and password input in fields
driver.find_element(*log_field).send_keys("login_nenye_999t_i_hope")
time.sleep(2)
driver.find_element(*email).send_keys("mym99ail@mail.i7c66")
time.sleep(2)
driver.find_element(*passwd).send_keys("123pa6ssegword123")
time.sleep(2)
driver.find_element(*submit).click()
time.sleep(5)

print(driver.find_element(*success_order_line))