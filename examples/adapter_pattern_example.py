#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: adapter_pattern_example.py
@time: 2018/3/15
"""


# 目标接口
class Duck(object):
    def fly(self):
        pass

    def quack(self):
        pass


class MallardDuck(Duck):
    def fly(self):
        print "I'm flying"

    def quack(self):
        print "Quack"


# 被适配接口
class Turkey(object):
    def gobble(self):
        pass

    def fly(self):
        pass


# 被适配对象
class WildTurkey(Turkey):
    def gobble(self):
        print "Gobble gobble"

    def fly(self):
        print "I'm flying a short distance"


# 适配器
class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self._turkey = turkey

    def fly(self):
        for i in xrange(4):
            self._turkey.fly()

    def quack(self):
        self._turkey.gobble()


if __name__ == '__main__':
    duck = MallardDuck()
    turkey = WildTurkey()

    duck.fly()
    duck.quack()

    turkey_adapter = TurkeyAdapter(turkey)
    turkey_adapter.fly()
    turkey_adapter.quack()
