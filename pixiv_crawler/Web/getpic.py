# Author: 小蜗牛 <2426936965@qq.com><https://github.com/zch9241>
# 
# 版权声明：该软件（pixiv_crawler）为「zch」所有，转载请附上本声明。
# 


import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import sys
import time

sys.path.append('../System/')

import System.path


class getpic(object):
    """
    * 图片获取模块
    """
    pyautogui.PAUSE = 0.5

    def __init__(self, browser):
        """
        * browser: main中创建的Chrome
        """
        self.browser = browser

    def mainget(self, artworks_num):
        """
        * artworks_num: 用户的插画数量
        """
        #所有插画class属性: rp5asc-10.jXaCme
        browser = self.browser

        #第一张插画
        getpic(browser).getpics()
        #之后的插画
        switch_num = artworks_num - 1
        for i in range(1, switch_num + 1):
            #按下right以切换下一张插画
            getpic(browser).switch()
            getpic(browser).getpics()

    def switch(self):
        """
        * 切换插画详情页
        """
        browser = self.browser

        pyautogui.press('right')
        time.sleep(5)
        link_now = browser.current_url
        print('[getpic-switch(massage)]: 当前url: %s'%link_now)

    def getfirstpic(self, url):
        """
        * url: 插画主页链接
        """
        print('[getpic-getfirstpic(massage)]: 正在运行...')

        browser = self.browser
        browser.get(url)

        #获取用户插画数量
        artworks = browser.find_element_by_class_name('sc-1mr081w-0.gWvsci')
        artworks_num = int(artworks.text)

        #print("[getpic-getfirstpic(massage)]: 请输入第一张插画所在元素class属性值（注意：元素中 ' '<空格> 用'.'<英文句号>  代替）")

        #element_firstpic = str(input('[getpic(input)]: 请输入上述元素属性：'))
        #print('[getpic-getfirstpic(massage)]: 等待网页加载，请返回Chrome...')
        #absolute_element = browser.find_element_by_class_name(element_firstpic)

        absolute_element = browser.find_element_by_class_name('rp5asc-10.jXaCme')

        #点击进入第一张插画详情页
        ActionChains(browser).move_to_element(absolute_element).click().perform()
        time.sleep(5)

        url_now = browser.current_url
        print('[getpic-getfirstpic(massage)]: 当前url: %s'%url_now)
        getpic(browser).mainget(artworks_num = artworks_num)


    def getpics(self):
        """
        * 点击进入大图
        """
        print('[getpic-getpics(massage)]: 正在运行...')
        browser = self.browser
        browser.refresh()

        realnum = 0

        try:
            expected_conditions.presence_of_element_located(
                browser.find_element_by_css_selector("div[aria-label='预览']")
            )
        except:
            #单张图片
            realnum = 1

        if realnum != 1:
            #若有多张图片，则获取图片数量
            num = browser.find_element_by_css_selector("div[aria-label='预览']>div>span")
            num_text = num.text
            #图片数量
            realnum = int(num_text[-1:])
            #button-查看全部
            element_button = WebDriverWait(browser, 20).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME,'emr523-2.dVBFOZ'))
                )
            print('[getpic-getpics(massage)]: button已找到。')
            #element_button = browser.find_element_by_class_name('emr523-2.dVBFOZ')
            ActionChains(browser).move_to_element(element_button).click().perform()

        #首张图片/单张图片
        pyautogui.moveTo(x=513, y=435,duration=0.25, tween=pyautogui.linear)
        pyautogui.click()

        print('[getpic-getpics(massage)]: 等待图片加载...')
        WebDriverWait(browser, 600).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'img'))
            )
        time.sleep(5)

        #original_pic = browser.find_element_by_css_selector("img")
        #ActionChains(browser).move_to_element(original_pic).context_click().perform()
        
        getpic(browser).savepic(realnum = realnum)


    def mouse(self):
        """
        * 移动鼠标
        """
        pyautogui.moveTo(x=651, y=284, duration=0.25, tween=pyautogui.linear)
        #pic1:Point(x=651, y=284)
        pyautogui.rightClick()
        pyautogui.press('down',presses=2)
        pyautogui.press('enter')
        time.sleep(7)

    def savepic(self, realnum):
        """
        * realnum: getpics中获取的图片数量（即调用几次保存程序）
        """
        browser = self.browser
        #运行Autoit程序保存图片
        if realnum == 1:
            #单张图片
            getpic(browser).mouse()

            print('[getpic-savepic(massage)]: 调用程序...')
            System.path.autoit().savepic_call()
            time.sleep(1)
            pyautogui.press('down')

        else:
            #非单张图片
            for i in range(1,realnum+1):
                try:
                    getpic(browser).mouse()
                    print('[getpic-savepic(massage)]: 调用程序...')
                    System.path.autoit().savepic_call()
                    time.sleep(0.25)
                    pyautogui.press('down')
                    time.sleep(5)
                except:
                    getpic(browser).mouse()
                    print('[getpic-savepic(warn)]: 调用程序失败...重试')
                    time.sleep(5)
                    System.path.autoit().savepic_call()
                    
                    #重复步骤
                    time.sleep(0.25)
                    pyautogui.press('down')
                    time.sleep(5)



