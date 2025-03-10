import sys
import setuptools
from wheel.bdist_wheel import bdist_wheel as bdist_wheel_orig


# 获取当前Python版本
current_python_version: str = ".".join(map(str, [sys.version_info.major, sys.version_info.minor]))
print(f"当前Python版本为：{current_python_version}")

# 如果Python版本是3.6
if current_python_version == "3.6":
    python_tag = "cp36"
    abi_tag = "cp36m"
# 如果Python版本是3.8
elif current_python_version == "3.8":
    python_tag = "cp38"
    abi_tag = "cp38"
# 如果Python版本是其他
else:
    raise RuntimeError("Unsupported Python version")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

class bdist_wheel(bdist_wheel_orig):
    def get_tag(self):
        # 返回 python tag, abi tag, platform tag
        return python_tag, abi_tag, "win_amd64"


setuptools.setup(
    name="tessng",
    version="4.0.3",
    author="Jida Transportation",
    author_email="17315487709@163.com",
    description="TESS NG V4.0 Secondary Development (Python version)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://jidatraffic.com:82/",
    python_requires=">=3.6, !=3.7.*, <3.9",
    packages=setuptools.find_packages(),
    package_data={
        "tessng": ["*.dll", "*.pyd", "*.pyi", "*.exe", "TESS_PythonAPI_EXAMPLE"]
    },
    install_requires=[
        "PySide2",
        "shiboken2",
    ],
    license='MIT',
    license_files=('LICENSE',),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        "bdist_wheel": bdist_wheel
    },
    zip_safe=False,
    include_package_data=True,
)
