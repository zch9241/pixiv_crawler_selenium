from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
 
caps = {
    'browserName': 'chrome',
    'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False, 
    },
}
option = webdriver.ChromeOptions()
option.add_argument(r"user-data-dir=C:\Users\x550\AppData\Local\Google\Chrome\User Data")    # 获取浏览器用户数据

option.add_argument('log-level=3')#INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
driver = webdriver.Chrome(desired_capabilities=caps,options=option)


driver.get('https://www.pixiv.net/users/4405891')
# 必须等待一定的时间，不然会报错提示获取不到日志信息，因为絮叨等所有请求结束才能获取日志信息
time.sleep(10)

request_log = driver.get_log()
print(request_log)

while True:
    pass