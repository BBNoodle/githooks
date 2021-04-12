# -*- coding: utf-8 -*- 
# @Time : 4/12/21 4:55 PM 
# @Author : mxt
# @File : config.py


class Config:
    def __init__(self, config: dict):
        self.result = dict()
        self.config = config
        self.father2son(config)

    def father2son(self, config):
        for k1, v1 in config.items():
            if isinstance(v1, dict):
                for k2, v2 in v1.items():
                    key = f"{k1}.{k2}"
                    self.result.setdefault(key, v2)
            else:
                self.result.setdefault(k1, v1)

    def get(self, item):
        return self.result.get(item)
