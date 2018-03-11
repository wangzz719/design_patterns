#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 10:55
# @Author  : wangzz
# @File    : singleton.py


def singleton(cls):
    '''
    Decorator support singleton
    :param cls:
    :return:
    '''
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton
