#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 16:05
# @Author  : wangzz
# @File    : strategy.py

class FlyBehavior(object):
    def fly(self):
        pass


class QuackBehavior(object):
    def quack(self):
        pass


class Duck(object):
    fly_behavior = FlyBehavior()
    quack_behavior = QuackBehavior()

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior
