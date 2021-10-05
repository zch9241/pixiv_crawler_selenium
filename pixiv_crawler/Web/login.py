# Author: 小蜗牛 <2426936965@qq.com><https://github.com/zch9241>
# 
# 版权声明：该软件（pixiv_crawler）为「zch」所有，转载请附上本声明。
# 


import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import time


class pixiv_login(object):
    def pixiv_login(self,browser, username, password):
        """
        * 登录模块
        * browser: main中创建的Chrome
        """

        print('[login(massage)]: 加载登录模块...')

        browser.get("https://www.pixiv.net/")

        pixiv_button = browser.find_element_by_class_name('signup-form__submit--login')
        ActionChains(browser).move_to_element(pixiv_button).click().perform()

        browser.find_element_by_css_selector('div.input-field>input[autocomplete="username"]').send_keys(username)
        browser.find_element_by_css_selector('div.input-field>input[autocomplete="current-password"]').send_keys(password)

        time.sleep(1)

        pyautogui.typewrite(['enter'])

        print('[login(massage)]: 登录成功！')

        time.sleep(5)

