# pixiv_crawler


这是基于`selenium 3.141.0`,使用`Python@3.8(+)` `AutoIT v3`编写的pixiv爬虫 

系统要求:Windows 7 (64位) 及以上

- 推荐使用最新版本的软件，以避免发生无法预期的错误 
- 本程序(pixiv_crawler)仅供学习交流，最初目的达成后请自行删除 
- 使用后任何不可知事件都与原作者无关，原作者不承担任何后果 
- 请自备访问`pixiv`的方法

### 使用

1.安装依赖
```
pip install pyautogui
pip install selenium
```
2.检查你的Chrome

(1) 请保证内核版本与`chromedriver`版本一致或接近
- chrome内核检查
```
chrome://settings/help
e.g:
Chrome 已是最新版本
版本 94.0.4606.71（正式版本） （64 位）
```
- chromedriver版本检查
```
#cmd
>cd \p\bin
>chromedriver -v
ChromeDriver 93.0.4577.63 (ff5c0da2ec0adeaed5550e6c7e98417dac77d98a-refs/branch-
heads/4577@{#1135})
```

(2)更新`chromedriver`
- `chromedriver`下载地址：
```
https://chromedriver.storage.googleapis.com/index.html
```

3.请在Chrome上先登录pixiv，以便程序调用个人数据。

### 注意
1.本程序调用的`AutoIT3`(.au3)编译的(.exe)程序运行时可能会被360报毒。详见`info.md`

你可以：
- 相信我
- 使用反编译查看源代码或者查看未编译的`au3`文件
- 使用知名的多引擎查杀工具（比如微步云）

2.本程序调用了`pyautogui`，故请在程序执行过程中不要轻易移动鼠标，操作键盘，以免带来未知的错误。

3.本程序运行时，请不要打开其他Chrome窗口。
