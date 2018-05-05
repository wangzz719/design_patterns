#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: iterator_pattern.py
@time: 2018/5/5
"""


# 共同的接口供所有的聚合使用，将客户代码从集合对象的实现解耦
class Aggregate(object):
    # 创建迭代器
    def create_iterator(self):
        pass


# 具体的集合持有一个对象集合，并实现create_iterator方法，利用此方法返回集合的迭代器
class ConcreteAggregate(Aggregate):
    def create_iterator(self):
        pass


# 迭代器接口
class Iterator(object):
    def has_next(self):
        pass

    def next(self):
        pass

    def remove(self):
        pass


# 具体的迭代器实现
class ConcreteIterator(Iterator):
    def has_next(self):
        pass

    def next(self):
        pass

    def remove(self):
        pass
