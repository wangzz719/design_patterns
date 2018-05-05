#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: composite_pattern.py
@time: 2018/5/5
"""


# Component（接口）为组合中所有对象定义一个接口，不管是组合还是叶节点
class Component(object):
    def operation(self):
        pass

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def get_child(self, int):
        pass


# 叶节点通过实现 Composite 支持的操作，定义了组合内元素的行为
class Leaf(Component):
    def operation(self):
        pass


# Composite 定义组件的行为，这样的组件具有子节点
# Composite 也实现了叶节点相关的操作
class Composite(Component):
    def add(self, component):
        pass

    def remove(self, component):
        pass

    def get_child(self, int):
        pass

    def operation(self):
        pass
