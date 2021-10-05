
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
 

#chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#chrome_options.add_experimental_option('useAutomationExtension', False)

driver = Chrome(executable_path = r"C:\Users\x550\Desktop\chromedriver_win32\chromedriver.exe")
 
with open(r'C:\Users\x550\Desktop\p\p\demo\stealth\stealth.min.js') as f:
    js = f.read()
 
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})

driver.get('https://bot.sannysoft.com/')


while True:
  pass