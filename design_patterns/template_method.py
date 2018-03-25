#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: template_method.py
@time: 2018/3/25
"""


class AbstractClass(object):
    # cannot be override by subclass
    def template_method(self):
        pass

    # implement in subclass
    def primitiveOperation1(self):
        pass

    # implement in subclass
    def primitiveOperation2(self):
        pass

    # cannot be modified by subclass
    def concreteOperation(self):
        print 'concrete operation'

    # can override by subclass
    def hook(self):
        print 'hook method'


class ConcreteClass(AbstractClass):
    def primitiveOperation1(self):
        print 'ConcreteClass Primitive Operation1'

    def primitiveOperation2(self):
        print 'ConcreteClass Primitive Operation2'

    def hook(self):
        print 'ConcreteClass hook method'
