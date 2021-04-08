# -*- coding: utf-8 -*- 
# @Time : 4/8/21 6:12 PM 
# @Author : mxt
# @File : __init__.py.py
from fileinput import input
from sys import stdout, stderr
from traceback import print_exc

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
