#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: adapter_pattern.py
@time: 2018/3/15
"""


# 目标
class Target(object):
    def request(self):
        pass


# 适配器
class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        self._adaptee.special_request()


# 被适配者
class Adaptee(object):
    def special_request(self):
        pass
