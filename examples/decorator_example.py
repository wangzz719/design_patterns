#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:51
# @Author  : wangzz
# @File    : decorator_example.py


class Beverage(object):
    def __init__(self):
        self._description = 'Unknown Beverage'

    @property
    def description(self):
        return self._description

    def cost(self):
        pass


class CondimentDecorator(Beverage):
    @property
    def description(self):
        return


class Espresso(Beverage):
    def __init__(self):
        super(Beverage, self).__init__()
        self._description = 'Espresso'

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super(Beverage, self).__init__()
        self._description = 'House Blend Coffee'

    def cost(self):
        return 0.89


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super(CondimentDecorator, self).__init__()
        self._beverage = beverage

    @property
    def beverage(self):
        return self._beverage

    @property
    def description(self):
        return self.beverage.description + ', Mocha'

    def cost(self):
        return .20 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        super(CondimentDecorator, self).__init__()
        self._beverage = beverage

    @property
    def beverage(self):
        return self._beverage

    @property
    def description(self):
        return self.beverage.description + ', Soy'

    def cost(self):
        return .55 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        super(CondimentDecorator, self).__init__()
        self._beverage = beverage

    @property
    def beverage(self):
        return self._beverage

    @property
    def description(self):
        return self.beverage.description + ', Whip'

    def cost(self):
        return .25 + self.beverage.cost()


if __name__ == '__main__':
    beverage = Espresso()
    print '{} ${}'.format(beverage.description, beverage.cost())

    beverage2 = HouseBlend()
    beverage2 = Soy(beverage2)
    beverage2 = Mocha(beverage2)
    print '{} ${}'.format(beverage2.description, beverage2.cost())
