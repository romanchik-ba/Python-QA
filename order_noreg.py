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
order_noreg = ("xpath", "/html/body/div[1]/section/div/div[2]/div/div/div/a[1]")
full_name = ("xpath", "//*[@id='orders-name']")
email = ("xpath", "//*[@id='orders-email']")
phone = ("xpath", "//*[@id='orders-phone']")
submit = ("xpath", "//*[@id='w0']/div[4]/button") 
delivery_type = ("xpath", "//*[@id='orders-delivery_type']")
address = ("xpath", "//*[@id='orders-address']")
payment_select = ("xpath", "//*[@id='orders-pay_type']")
final_order = ("xpath", "//*[@id='w0']/div[2]/button")
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

# Clicking on "Order" button
driver.find_element(*order_noreg).click()
time.sleep(2)

# Entering full name into "Full name" field
driver.find_element(*full_name).send_keys("Name Surname")
time.sleep(2)

# Entering e-mail into email field
driver.find_element(*email).send_keys("12345@mail.nk")
time.sleep(2)

# Entering phone into phone field
driver.find_element(*phone).send_keys("12345")
time.sleep(2)

# Clicking on "Order" button
driver.find_element(*submit).click()
time.sleep(5)

## Finds the element specified by select_locator, wraps it in a Select object, 
# and then selects the option with a value of “Почтой” from the dropdown menu.
dropdown = Select(driver.find_element(*delivery_type))
dropdown.select_by_visible_text("Почтой")
time.sleep(1.5)

# Entering address into address field
driver.find_element(*address).send_keys("Destination Point")
time.sleep(2)

# Clicking on "Submit" button
driver.find_element(*submit).click()
time.sleep(5)

# Clicking on "End the order" button
driver.find_element(*final_order).click()
time.sleep(2)

print(driver.find_element(*success_order_line))