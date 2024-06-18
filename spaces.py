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
driver = webdriver.Chrome(options = options)

# Set up ChromeDriver and launch Chrome browser.
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Locators
search_btn = ("xpath", "/html/body/header/div[3]/div/div/div/div/a[3]")
search_input = ("xpath", "/html/body/header/div[3]/div/div/div/div/div/form/input")

driver.get("https://tritonshoes.ru")

### Test Case '3'
# Click on the Search button
driver.find_element(*search_btn).click()
time.sleep(2)

# Input of SPACE symbols into the field
driver.find_element(*search_input).send_keys("                ")
time.sleep(2)

# Start search by pressing ENTER key
driver.find_element(*search_input).send_keys(Keys.ENTER)
time.sleep(8.5)

# Get current URL
current_url = driver.current_url
print(current_url)

# Number of "+" symbols in URL
count_plus = current_url.count("+")

print(f"Number of '+' synmbols in URL-address: {count_plus}")