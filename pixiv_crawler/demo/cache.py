import os
from selenium import webdriver
os.makedirs('cache', exist_ok=True)
options = webdriver.ChromeOptions()
options.add_argument('--disk-cache-dir=./cache')
options.add_argument(r"user-data-dir=C:\Users\x550\AppData\Local\Google\Chrome\User Data")    # 获取浏览器用户数据
options.add_argument('--ignore-certificate-errors')
options.add_argument('log-level=3')#INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0

driver = webdriver.Chrome(options=options)

driver.get('https://www.pixiv.net/users/4405891')

while True:
    pass