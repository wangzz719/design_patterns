#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: singleton_metaclass_example.py
@time: 2018/3/12
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: singleton_baseclass_example.py
@time: 2018/3/12
"""

import sys

sys.path.append('../design_patterns')

import threading

from design_patterns.singleton_metaclass import Singleton


class A():
    __metaclass__ = Singleton

    def __init__(self, x):
        self.x = x

    def go(self):
        print self.x


def worker():
    a = A(1)
    print 'a.id: ' + str(id(a)) + '\n'


def singleton_simple_test():
    a1 = A(1)
    a2 = A(2)
    print 'a1.x: ' + str(a1.x) + '\n'
    print 'a2.x: ' + str(a2.x) + '\n'
    print 'a1.id: ' + str(id(a1)) + '\n'
    print 'a2.id: ' + str(id(a2)) + '\n'


def singleton_concurrent_test():
    task = []
    for i in range(30):
        t = threading.Thread(target=worker)
        task.append(t)

    for t in task:
        t.start()

    for t in task:
        t.join()


def test_singleton():
    print '==== * singleton_concurrent_test * ===='
    singleton_concurrent_test()

    print '==== * singleton_simple_test * ===='
    singleton_simple_test()


if __name__ == '__main__':
    test_singleton()
