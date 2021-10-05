;Author: 小蜗牛
;参考: https://blog.csdn.net/s740556472/article/details/79322047
;ControlFocus ( "title", "窗口文本", controlID)   设置输入焦点到指定窗口的某个控件上
;WinWait ( "title题" , "窗口文本" , 超时时间 )  暂停脚本的执行直至指定窗口存在（出现）为止
;#ControlSetText ( "title", "窗口文本", controlID, "新文本" )   修改指定控件的文本
;Sleep ( 延迟 )   使脚本暂停指定时间段
;ControlClick ( "title", "窗口文本", 控件ID , 按钮 , 点击次数 )   向指定控件发送鼠标点击命令
;其中，title即AutoIt Window Info识别出的Title字段，controlID即AutoIt Window Info识别出的Class和Instance的拼接，如上图拼接后的结果应为：Button1
;第一步:聚焦另存为窗口,title:另存为,"text",controlId:写ID可以识别
ControlFocus("另存为","text","32770")
;暂停脚本的执行直至指定窗口存在（出现）为止
WinWait("[CLASS:#32770]","",10)
;第二步:填充文件名地址,其中$CmdLine[1]代表exe执行时的动态参数,
;例如 kuang.exe "D:/test/a.html",这样就可以动态改变地址的名字，通过python
;ControlSetText("另存为","","Edit1",CmdLine[1])
;延时函数
Sleep(1000)
;第三步:点击保存按钮,进行下载,title:另存为,"text"写成空,controlId:写成Button2（ClassnameNN）也可以识别
ControlClick("另存为","","Button1")


