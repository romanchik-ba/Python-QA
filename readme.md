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
