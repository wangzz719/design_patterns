#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: abstract_factory.py
@time: 2017/11/19
"""


class AbstractFactory(object):
    def create_product_A(self):
        pass

    def create_product_B(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_A(self):
        print 'ConcreteFactory1 created product A'

    def create_product_B(self):
        print 'ConcreteFactory1 created product B'


class ConcreteFactory2(AbstractFactory):
    def create_product_A(self):
        print 'ConcreteFactory2 created product A'

    def create_product_B(self):
        print 'ConcreteFactory2 created product B'
