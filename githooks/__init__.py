# -*- coding: utf-8 -*- 
# @Time : 4/8/21 6:12 PM 
# @Author : mxt
# @File : __init__.py.py
import os
import yaml
from sys import stdout, stderr
from traceback import print_exc

from githooks.default import DEFAULT_CONFIG
from githooks.check import CheckState
from githooks.check import BaseCheck
from githooks.config import Config


class Runner(object):
    def __init__(self):
        self.default_path = "/var/opt/githooks/default.yml"
        self.config = Config(self.get_configuration())

    def get_configuration(self):
        default_exists = os.path.exists(self.default_path)
        if default_exists:
            with open(self.default_path, 'r', encoding='utf-8') as cfg:
                content = cfg.read()
                return yaml.load(content)
        else:
            return DEFAULT_CONFIG

    def run(self):
        a = self.config.get("dev.dev_mode")
        return 0


def main():
    try:
        state = Runner().run()
    except Exception as e:
        # Flush the problems we have printed so far to avoid the traceback
        # appearing in between them.
        stdout.flush()
        print(file=stderr)
        print('{} An error occurred: {}'.format(BaseCheck.ERROR_MSG_PREFIX, e), file=stderr)
        print_exc()
        return 1
    else:
        if state >= CheckState.FAILED:
            return 1
    return 0
