from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities        
import json
import re

options = webdriver.ChromeOptions()
# options.add_argument('--headless')   #无头模式
# options.add_argument('--no-sandbox') #非沙盒
# options.add_argument('--disable-gpu') #禁用gpu，一般生产环境会使用，因为服务器大多没有gpu
prefs = {"profile.managed_default_content_settings.images": 2} #不加载图片
options.add_experimental_option("prefs", prefs)
#重点来了
options.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True})
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument(r"user-data-dir=C:\Users\x550\AppData\Local\Google\Chrome\User Data")    # 获取浏览器用户数据
options.add_argument('--ignore-certificate-errors')
options.add_argument('log-level=3')#INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0

caps = DesiredCapabilities.CHROME

#重点又来了
caps['goog:loggingPrefs'] = {'performance': 'ALL'}   
driver = webdriver.Chrome(options=options, desired_capabilities=caps)
#driver.implicitly_wait(5)
# driver = webdriver.Chrome(desired_capabilities=caps)



def get_body(log, driver):
    #获得log里面的requestid，通过id来获得response的内容
    requestId = json.loads(log.get("message")).get("message").get("params").get("requestId")
    # 
    driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})
    response_dict = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})
    #注意，这里获得的body是字符串形式，需要序列化为json对象/
    body = response_dict["body"]        
    Jres = json.loads(body)
    return Jres


driver.get('https://www.pixiv.net/users/4405891')
#chrome的日志将开启并记录所有的访问。

logs = driver.get_log("performance")
for log in logs[:]:
    try:
        url = json.loads(log.get("message")).get("message").get("params").get("request").get("url")
    except:
        url = None

    # 正则表达是匹配 需要抓取的那一个请求 
    regex_person_document = re.compile(
            'https://www.pixiv.net/ajax/user/4405891/profile/all?lang=zh'
        )
    url = str(url)
    regex_person_document.findall(url)
    # 获得了 json形式的响应体，就能按需要获得里面的数据了
    Jres = get_body(log, driver)
    print(Jres)

