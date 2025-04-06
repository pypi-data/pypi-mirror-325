from os import path as os_path
from setuptools import setup, find_packages

this_directory = os_path.abspath(os_path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup(
    name="allure-pytest-yaml",
    version="1.1.1",
    author="Fei Wu",
    url='https://gitee.com/easyfei/pytest-yaml-fei.git',
    author_email="504294190@qq.com",
    description="a pytest yaml allure package",
    license='MIT License',  # 许可协议
    install_requires=['Jinja2', 'jmespath', 'jsonpath', 'pytest', 'PyYAML', 'requests', 'allure-pytest', 'pymysql',
                      'DingtalkChatbot'],  # 依赖包
    # long_description=read_file('README.md'),  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    scripts=['pytest_yaml_fei.start_project:create_start_project'],
    script_name='pytest --start-project',
    # 要求安装依赖包之后 在命令行输入pytest --start-project可以初始化项目
    entry_points={
        "console_scripts": ['pytest --start-project = pytest_yaml_fei.start_project:create_start_project']
    },  # 安装成功后，在命令行输入pytest --start-project 就相当于执行了pytest_yaml_fei.start_project.py中的create_project了
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # 对python的最低版本要求
)
