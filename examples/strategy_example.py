#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 16:12
# @Author  : wangzz
# @File    : strategy_example.py

import sys

sys.path.append('../design_patterns')

from design_patterns.strategy import Duck, FlyBehavior, QuackBehavior


class FlyWithWings(FlyBehavior):
    def fly(self):
        print 'I am flying'


class FlyNoWay(FlyBehavior):
    def fly(self):
        print 'I can not fly'


class Quack(QuackBehavior):
    def quack(self):
        print 'Quack'


class Squeak(QuackBehavior):
    def quack(self):
        print 'Squeak'


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Squeak()


if __name__ == '__main__':
    duck = Duck()
    duck.perform_fly()
    duck.perform_quack()

    mallard_duck = MallardDuck()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()

    model_duck = ModelDuck()
    model_duck.perform_fly()
    model_duck.fly_behavior = FlyNoWay()
    model_duck.perform_fly()
    model_duck.perform_quack()
    model_duck.quack_behavior = Quack()
    model_duck.perform_quack()
