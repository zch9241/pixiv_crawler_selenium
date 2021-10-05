# Author: 小蜗牛 <2426936965@qq.com><https://github.com/zch9241>
# 
# 版权声明：该软件（pixiv_crawler）为「zch」所有，转载请附上本声明。
# 


import os


class autoit(object):
    """
    * 运行autoit程序
    """
    def path_bin(self):
        project_path = os.getcwd()
        bin_path = project_path + r'\p\bin'
        return bin_path

    def savepic_call(self):
        Bin_path = autoit().path_bin()
        savepicExe_path = Bin_path + r'\savepic.exe'
        os.system(savepicExe_path)
        
    def msg1_call(self):
        Bin_path = autoit().path_bin()
        msg1Exe_path = Bin_path + r'\msg1.exe'
        os.system(msg1Exe_path)

class mainpath(autoit):
    """
    * main.py 所调用的程序路径
    """
    def chromedriver_path(self):
        """
        * return: chromedriver.exe所在绝对路径
        """
        project_path = mainpath().path_bin()
        Chromedriver_path = project_path + r'\chromedriver.exe'
        return Chromedriver_path
    def StealthMinJs_path(self):
        """
        * return: stealth.min.js所在绝对路径
        """
        project_path = mainpath().path_bin()
        stealthMinJs_path = project_path + r'\stealth.min.js'
        return stealthMinJs_path
