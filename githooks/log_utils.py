# -*- coding: utf-8 -*- 
# @Time : 5/27/21 3:13 PM 
# @Author : mxt
# @File : log_utils.py

import os
import sys
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
LOG_FILE_NAME = os.environ.get('LOG_FILE_NAME', 'logs/pre-receive.log')
LOG_FORMAT = os.environ.get('LOG_FORMAT', '%(asctime)s [%(levelname)s]: %(message)s')


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def log_init():
    ensure_dir(LOG_FILE_NAME)
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)
    # 一天一个日志文件
    file_handler = TimedRotatingFileHandler(LOG_FILE_NAME, when='D', interval=1)
    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
