# -*- coding: utf-8 -*- 
# @Time : 4/13/21 5:22 PM 
# @Author : mxt
# @File : setup.py
import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xt-githooks",
    version="0.2.7",
    author="BBNoodle",
    author_email="1214403402@qq.com",
    description="Git pre-receive hook to check commits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BBNoodle/githooks.git",
    keywords=(
        'git git-hook python pre-receive hook'
    ),
    entry_points={
        'console_scripts': [
            'pre-receive=githooks:main',
        ],
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    python_requires=">=3.6",
    include_package_data=True
)
