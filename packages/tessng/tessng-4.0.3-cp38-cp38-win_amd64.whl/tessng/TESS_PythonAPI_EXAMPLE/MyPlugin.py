import os
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import Qt
from tessng import TessPlugin, TessngFactory, tessngIFace
from MyNet import MyNet
from MySimulator import MySimulator


# 用户插件，继承自TessPlugin
class MyPlugin(TessPlugin):
    def __init__(self):
        super().__init__()
        self.my_net = None
        self.my_simulator = None

    def start(self, config: dict) -> None:
        # 工作空间目录路径
        workspace = os.path.join(os.getcwd(), "WorkSpace")
        config["__workspace"] = workspace
        # 创建文件夹
        os.makedirs(workspace, exist_ok=True)

        # 创建TESS NG对象
        app = QApplication()
        factory = TessngFactory()
        tessng = factory.build(self, config)
        if tessng is None:
            sys.exit(0)
        else:
            sys.exit(app.exec_())

    # 过载父类方法：在 TESS NG工厂类创建TESS NG对象时调用
    def init(self) -> None:
        self.my_net = MyNet()
        self.my_simulator = MySimulator()
        # 关联信号和槽函数
        iface = tessngIFace()
        win = iface.guiInterface().mainWindow()
        # 将信号mSimuInf.forReStopSimu关联到主窗体的槽函数doStopSimu，可以安全地停止仿真
        self.my_simulator.forStopSimu.connect(win.doStopSimu, Qt.QueuedConnection)
        # 将信号mSimuInf.forReStartSimu关联到主窗体的槽函数doStartSimu，可以安全地启动仿真
        self.my_simulator.forReStartSimu.connect(win.doStartSimu, Qt.QueuedConnection)

    # 过载父类方法：返回插件路网子接口，此方法由TESS NG调用
    def customerNet(self):
        return self.my_net

    # 过载父类方法：返回插件仿真子接口，此方法由TESS NG调用
    def customerSimulator(self):
        return self.my_simulator
