    ## !!! CHECK README.MD BEFORE EXECUTING THE TEST !!!
# Import necessary libraries
import time
import pickle
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.page_load_strategy = "eager"
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("-user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0")

# Set up ChromeDriver and launch Chrome browser.
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Locators
men_shoes = ("xpath", "/html/body/header/div[3]/div/div/div/nav/ul/li[2]/a")
boots = ("xpath", "/html/body/div[1]/section/div/div[2]/div/div[2]/div[1]/div/div/a[2]")
corz_fb = ("xpath", "//*[@id='w0']/div[1]/div[1]/div[4]/a[2]")
cart = ("xpath", "//a[@id='miniCart']")
buy = ("xpath", "//*[@id='tov_pop3573']/section/div[2]/a[1]")
close_btn = ("xpath", "//*[@id='tov_pop3573']/button")

driver.get("https://tritonshoes.ru")

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

# Retrieving cookies from a driver, filters them based on predefined names, and saves the filtered cookies to a pickle file for later use.
cookies_names = ["PHPSESSID", "_csrf", "_ym_d", "_ym_isad", "_ym_uid", "_ym_visorc"]
all_cookies = driver.get_cookies()
filtered_cookies = [cookie for cookie in all_cookies if cookie['name'] in cookies_names]
with open(os.path.join(os.getcwd() + "cookies_list.pkl"), "wb") as file:
    pickle.dump(filtered_cookies, file)

# Deleting all cookies
driver.delete_all_cookies()
driver.refresh()
time.sleep(5)

# Loads cookies from the file
with open(os.path.join(os.getcwd(), "cookies_list.pkl"), "rb") as file:
    cookies_list = pickle.load(file)

# Adding each cookie from cookies_list
for cookie in cookies_list:
    driver.add_cookie(cookie)

# Refreshing the page to apply cookies
driver.refresh()
time.sleep(6)