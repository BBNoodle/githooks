# -*- coding: utf-8 -*- 
# @Time : 4/13/21 5:22 PM 
# @Author : mxt
# @File : setup.py
import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xt-githooks",
    version="0.2.2",
    author="Maoxinteng",
    author_email="1214403402@qq.com",
    description="Git Hooks Pre-receive",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BBNoodle/githooks.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
