# **Initialization of Chrome WebDriver Selenium (<i><span style="color:#60c3e0">! MS Windows & Google Chrome only</i>)**

## 1. Install VS Code and Python Interpreter at first:

🟠 <b>[Python](https://www.microsoft.com/store/productId/9NCVDN91XZQP?ocid=pdpshare)</b>

🟠 <b>[VS Code](https://code.visualstudio.com)</b>

## 2. Open VS Code, create new project, then open terminal (`Ctrl` + `Shift` + `~`) and run this command in terminal:
```bash 
    python3.12 -m venv venv
```
Wait until the `venv` folder appears in current working directory. It'll means, virtual environment (V.E.) was created succesfully.

## 3.  To activate V.E., you'll have to execute next command:
```bash 
    venv/Scripts/activate.ps1
```
If the message <span style="color:#28c78d"><b>(venv)</span> is displayed next to the command line, the virtual environment is activated.

## 4. To install Selenium and WebDriver Manager dependencies, run command:
```bash 
    pip3 install selenium webdriver-manager
```

## All done! Below are all of the neccessary objects and libraries for tests:

Library|Description
:---|:---
<span style="color:#b98de3">import <span style="color:#68ccb6">pickle</span>|The pickle module provides a powerful algorithm for serializing and deserializing Python objects. “Pickling” is the process of converting a Python object into a byte stream, while “unpickling” is the reverse operation that converts the byte stream back into a Python object. Since the byte stream can easily be written to a file, the pickle module is commonly used to save and load complex objects in Python.
<span style="color:#b98de3">from</span> <span style="color:#68ccb6">selenium <span style="color:#b98de3">import <span style="color:#68ccb6">webdriver</span>|Imports the webdriver class from the selenium library.
<span style="color:#b98de3">from</span> <span style="color:#68ccb6">webdriver_manager.chrome <span style="color:#b98de3">import <span style="color:#68ccb6">ChromeDriverManager</span>|Imports the ChromeDriverManager from the webdriver_manager.chrome module.
<span style="color:#b98de3">from</span> <span style="color:#68ccb6">selenium.webdriver.chrome.service <span style="color:#b98de3">import <span style="color:#68ccb6">Service</span>|The Service class is used to manage the lifecycle of the ChromeDriver. It allows to start, connect to, and stop the ChromeDriver server, which is needed for Selenium to interact with the Chrome browser.
<span style="color:#5b8ac7">service</span> = <span style="color:#68ccb6">Service</span>(<span style="color:#5b8ac7">executable_path</span>=<span style="color:#68ccb6">ChromeDriverManager</span>().install())  <span style="color:#5b8ac7">driver</span> = <span style="color:#68ccb6">webdriver.Chrome</span><span style="color:#5b8ac7">(service=service)</span>|Automatically download and install the latest version of ChromeDriver (if it’s not already installed), start the ChromeDriver service, and then launch a new Chrome browser window that can be controlled by the driver object.
<span style="color:#b98de3">from</span> <span style="color:#68ccb6">selenium.webdriver.chrome.options <span style="color:#b98de3">import <span style="color:#68ccb6">Options</span>|The Options class allows you to set various options for the Chrome browser. You can use it to customize the behavior of the browser, such as setting the browser to headless mode (which means the browser runs in the background and doesn’t display a GUI), disabling JavaScript, or specifying a specific window size.
<span style="color:#b98de3">from</span> <span style="color:#68ccb6">selenium.webdriver.common.action_chains <span style="color:#b98de3">import <span style="color:#68ccb6">ActionChains</span>|The ActionChains class in Selenium is a way to automate low level interactions such as mouse movements, mouse button actions, key press, and context menu interactions. This is useful for doing more complex actions like hover over and drag and drop.
<span style="color:#b98de3">from</span> <span style="color:#68ccb6">selenium.webdriver.support <span style="color:#b98de3">import <span style="color:#68ccb6">expected_conditions as EC </span>|Expected_conditions is a set of predefined conditions used with the Selenium WebDriver’s explicit waits. An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution.
<span style="color:#b98de3">from</span> <span style="color:#68ccb6">selenium.webdriver.support.ui <span style="color:#b98de3">import <span style="color:#68ccb6">WebDriverWait </span>|WebDriverWait is used in conjunction with expected_conditions to implement explicit waits in Selenium WebDriver. An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution.
