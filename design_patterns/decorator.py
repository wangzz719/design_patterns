#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:28
# @Author  : wangzz
# @File    : decorator.py

class Component(object):
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        '''
        add your own code here
        :return:
        '''
        print 'ConcreteComponent operation'


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self):
        '''
        add your own code here
        :return:
        '''
        self.component.operation()
        print 'Decorator operation'


class ConcreteDecoratorA(Decorator):
    def __init__(self, component):
        super(Decorator, self).__init__()
        self._component = component

    def operation(self):
        '''
        add your own code here
        :return:
        '''
        self.component.operation()
        print 'ConcreteDecoratorA operation'
