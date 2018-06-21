# -*- coding: utf-8 -*-

import setuptools
import os
import requests

# 将markdown格式转换为rst格式
def md_to_rst(from_file, to_file):
    r = requests.post(url='http://c.docverter.com/convert',
                      data={'to':'rst','from':'markdown'},
                      files={'input_files[]':open(from_file,'rb')})
    if r.ok:
        with open(to_file, "wb") as f:
            f.write(r.content)


md_to_rst("README.md", "README.rst")

long_description = 'set console color of font'
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setuptools.setup(
    name="consolecolor",
    version="0.0.2",
    author="Peng Shiyu",
    license = 'MIT License',
    author_email="pengshiyuyx@gmail.com",
    description="set console color of font",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/mouday/consolecolor",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires = [],       # 常用
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
            'img': ['*.png'],
        }

)

"""
python setup.py sdist bdist_wheel

twine upload dist/*

"""