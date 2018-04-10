# -*- coding: utf-8 -*-

from setuptools import setup, find_packages  

setup(  
    name = 'consolecolor',  
    version = '0.0.1',
    # keywords = ('consolecolor',),  
    description = 'set console color of font',  
    license = 'MIT License',  
    install_requires = [],  
    packages = ['consolecolor'],  # 要打包的项目文件夹
    include_package_data=True,   # 自动打包文件夹内所有数据
    author = 'pengshiyu',  
    author_email = '1940607002@qq.com',
    url = 'https://github.com/mouday/consolecolor'
)  