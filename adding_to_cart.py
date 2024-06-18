    ## !!! CHECK README.MD BEFORE EXECUTING THE TEST !!!
# Import necessary libraries
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(options = options)

# Set up ChromeDriver and launch Chrome browser.
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

# Locators
men_shoes = ("xpath", "/html/body/header/div[3]/div/div/div/nav/ul/li[2]/a")
boots = ("xpath", "/html/body/div[1]/section/div/div[2]/div/div[2]/div[1]/div/div/a[2]")
corz_fb = ("xpath", "//*[@id='w0']/div[1]/div[1]/div[4]/a[2]")
buy = ("xpath", "//*[@id='tov_pop3573']/section/div[2]/a[1]")

driver.get("https://tritonshoes.ru")

# Click on the Men Shoes button
driver.find_element(*men_shoes).click()
time.sleep(2)

# Clicking on item "Ботинки"
driver.find_element(*boots).click()
time.sleep(2)

# Clicking on cart button
driver.find_element(*corz_fb).click()
time.sleep(2)

# Clicking on buy button
wait.until(EC.element_to_be_clickable(buy)).click()
time.sleep(2)

