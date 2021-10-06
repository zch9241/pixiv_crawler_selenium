# Author: 小蜗牛 <2426936965@qq.com><https://github.com/zch9241>
# 
# 版权声明：该软件（pixiv_crawler）为「zch」所有，转载请附上本声明。
# Apache 2.0
# 
# Version: 1.0
# Release: 1001
# 
# 版本更新说明：
# v1.0 程序首个版本
# 


from selenium import webdriver
import time

import Web.login
import Web.getpic
import System.path


#options
option = webdriver.ChromeOptions()
option.add_argument(r"user-data-dir=C:\Users\x550\AppData\Local\Google\Chrome\User Data")    # 获取浏览器用户数据
option.add_argument('--ignore-certificate-errors')
option.add_argument('log-level=3')#INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
#初始化
driver_path = System.path.mainpath().chromedriver_path()

browser = webdriver.Chrome(executable_path = driver_path, chrome_options = option)
browser.maximize_window()
#反->反selenium
stealth_min_js_path = System.path.mainpath().StealthMinJs_path()
with open(stealth_min_js_path) as f:
    js = f.read()

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})

#username = str(input('[main->login(massage)]:您的用户名：'))
#password = str(input('[main->login(massage)]:您的密码：'))

user_id = int(input('[main(massage)]: 所要爬取的用户id: '))
#user_id = 171701
url = 'https://www.pixiv.net/users/' + str(user_id) +'/illustrations'


#login = login.pixiv_login()
#login.pixiv_login(browser = browser)
Web.getpic.getpic(browser).getfirstpic(url = url)
print(' [main(massage)]: 程序调试结束...退出Chrome。')
time.sleep(5)
browser.quit()
