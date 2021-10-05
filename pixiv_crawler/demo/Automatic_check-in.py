# Author: 小蜗牛 <2426936965@qq.com><https://github.com/zch9241>
# 
# 版权声明：该软件（Automatic_check-in）转载须获得本作者许可
# 
# Version: 1.0
# Release: 1001
# 
# 版本更新说明：
# v1.0 程序首个版本
# 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


#--user information--
username = 'zch'
password = '123456'

browser = webdriver.Chrome(executable_path = r"C:\Users\x550\Desktop\chromedriver_win32\chromedriver.exe")

browser.get("https://www.acgtubao.com/")

time.sleep(3)

browser.refresh()
#-------login_start-------
#'html.avgrund-ready/body.home.blog.logo-left/div#page.site/div.site-header.mg-b/div.site-header-in/div.header.logo-left/div.top-style/div.wrapper/div.header-user/div.top-user-info/div.login-button/div.header-login-button/button.empty.mobile-hidden'
element = browser.find_element_by_class_name('empty.mobile-hidden')
ActionChains(browser).move_to_element(element).click().perform()

login_element_username = browser.find_element_by_name('username').send_keys(username)
login_element_password = browser.find_element_by_name('password').send_keys(password)

login_element_button = browser.find_element_by_class_name('login-bottom')
ActionChains(browser).move_to_element(login_element_button).click().perform()

print('[massage]Login complete!')
time.sleep(3)
#-------login_end-------

#-------task_start-------
browser.get('https://www.acgtubao.com/task')
time.sleep(10)

task_element = browser.find_element_by_class_name('link-block')
ActionChains(browser).move_to_element(task_element).click().perform()

print('[massage]Task accomplished!')
time.sleep(3)
#-------task_end-------

print('[massage]Program run completed!')
string = str(input(print('[massage]press Enter to exit!')))

if string == '':
    browser.quit()
