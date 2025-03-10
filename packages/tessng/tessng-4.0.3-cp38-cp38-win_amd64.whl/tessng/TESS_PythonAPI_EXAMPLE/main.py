# TESS NG 二次开发说明：http://jidatraffic.com:82/
from MyPlugin import MyPlugin


if __name__ == '__main__':
    config = {
        # tess路网文件路径
        "__netfilepath": "",
        # 加载路网后是否自动开启仿真
        "__simuafterload": True,
        # 是否自定义仿真函数调用频率
        "__custsimubysteps": False,
    }
    my_plugin = MyPlugin()
    my_plugin.start(config)
