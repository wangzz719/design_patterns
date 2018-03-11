#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: singleton_baseclass.py
@time: 2018/3/12
"""


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not class_._instance:
            class_._instance = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instance
