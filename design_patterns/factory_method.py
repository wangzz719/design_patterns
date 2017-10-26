#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wangzhizhao@zhihu.com
@file: factory_method.py
@time: 2017/10/26
"""


class Product(object):
    def product_method(self):
        pass


class ConcreteProductA(Product):
    def product_method(self):
        print 'ConcreteProductA product method'


class ConcreteProductB(Product):
    def product_method(self):
        print 'ConcreteProductB product method'


class Creator(object):
    def factory_method(self, type):
        pass

    def an_operation(self, type):
        product = self.factory_method(type)
        product.product_method()


class ConcreteCreator(Creator):
    def factory_method(self, type):
        if type == 'a':
            product = ConcreteProductA()
        else:
            product = ConcreteProductB()

        return product
