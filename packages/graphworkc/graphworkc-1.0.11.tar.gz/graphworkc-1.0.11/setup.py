import glob
from setuptools import setup, find_packages
from pybind11.setup_helpers  import Pybind11Extension, build_ext
from pybind11 import get_include

ext_modules = [
    Pybind11Extension(
        "graphworkc",  # 模块导入名称
        ["src/main.cpp", "src/CNetwork.cpp"],
        define_macros=[('EXAMPLE_MACRO', '1')],# 可选参数，例如定义宏
        include_dirs=["src/"],  # 确保编译器能找到头文件
    ),
]

setup(
    name="graphworkc",
    version="1.0.11",
    author="ZC",
    description="A Python package with pybind11 extensions",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    python_requires=">=3.6",  # 指定支持的Python版本
    install_requires=["pybind11>=2.5.0"],  # 确保安装pybind11
    # options={
    #     "build_ext": {"timeout": 300}  # 单位：秒
    # },
)

# if (1):
#     # 获取当前目录
#     current_dir = Path(__file__).parent
#
#     # 自动查找所有 .pyd 文件
#     pyd_files = glob.glob(str(current_dir / "graphworkc" / "*.pyd"))
#
#     setup(
#         name="graphworkc",
#         version="1.0.10",
#         description="A Python wrapper for Graphworkc extension.",
#         author="ZC",
#         author_email="1263703239@qq.com",
#         packages=find_packages(),
#         py_modules=["__init__"],
#         include_package_data=True,
#         package_data={
#             "graphworkc": pyd_files,  # 自动添加所有 .pyd 文件
#         },
#         classifiers=[
#             "Programming Language :: Python :: 3.10",
#             "Programming Language :: Python :: 3.11",
#             "Operating System :: Microsoft :: Windows",
#         ],
#         python_requires=">=3.6",
#     )


# if (1):
#     # 获取当前目录
#     current_dir = Path(__file__).parent
#
#     # 自动查找所有 .pyd 文件
#     pyd_files = glob.glob(str(current_dir / "graphworkc" / "*.pyd"))
#
#     setup(
#         name="graphworkc",
#         version="1.0.10",
#         description="A Python wrapper for Graphworkc extension.",
#         author="ZC",
#         author_email="1263703239@qq.com",
#         packages=find_packages(),
#         py_modules=["__init__"],
#         include_package_data=True,
#         package_data={
#             "graphworkc": pyd_files,  # 自动添加所有 .pyd 文件
#         },
#         classifiers=[
#             "Programming Language :: Python :: 3.10",
#             "Programming Language :: Python :: 3.11",
#             "Operating System :: Microsoft :: Windows",
#         ],
#         python_requires=">=3.6",
#     )
