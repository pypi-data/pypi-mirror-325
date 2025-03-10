import os
import shutil
from PySide2.QtWidgets import QApplication
from tessng.Tessng import *


print("\033[94mWelcome to the tessng package! You can generate sample files using the \"tessng.get_demo_files()\".\033[0m")
print("\033[92mFor more detailed usage instructions, please visit: http://jidatraffic.com:82/.\033[0m")
print()


def get_demo_files(path: str = None) -> None:
    """
    生成TESS NG 二次开发的基础案例代码文件
    :param path: 代码文件的生成路径
    :return: 无
    """
    # 没有指定路径，则默认生成到当前路径
    if path is None:
        path: str = os.getcwd()
        word: str = "默认"
    # 指定了路径
    else:
        # 检查路径是否存在
        if not os.path.exists(path):
            print(f"指定路径不存在：{path}")
            return
        word: str = "指定"

    # 获取当前脚本的同级路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(current_dir, "TESS_PythonAPI_EXAMPLE")

    # 检查源文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"案例文件不存在，无法生成")
        return

    # 遍历源文件夹中的所有文件
    all_files = os.listdir(source_folder)
    file_count: int = 4
    for i, filename in enumerate(all_files, start=1):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(path, filename)

        # 检查目标路径是否已经存在
        if os.path.exists(destination_file):
            print(f"【{i}/{file_count}】 文件 {filename} 已存在，请手动检查并移除！")
            return

        # 判断是否是文件
        if os.path.isfile(source_file):
            # 拷贝文件
            shutil.copy2(source_file, destination_file)
            print(f"【{i}/{file_count}】 文件 {filename} 已生成！")

    print()
    print(f"基础案例代码文件已经生成到{word}路径：{path}")
    print(f"更多使用说明请访问：http://jidatraffic.com:82/document/V4.x/Python3/details.html")
    print()
