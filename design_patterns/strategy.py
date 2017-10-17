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
    @property
    def fly_behavior(self):
        if not hasattr(self, '_fly_behavior'):
            return FlyBehavior()
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior):
        self._fly_behavior = fly_behavior

    @property
    def quack_behavior(self):
        if not hasattr(self, '_quack_behavior'):
            return QuackBehavior()
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior):
        self._quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()
