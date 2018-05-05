#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: template_method_example.py
@time: 2018/3/25
"""


class CaffeineBeverageWithHook(object):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def brew(self):
        pass

    def add_condiments(self):
        pass

    def boil_water(self):
        print 'boiling water'

    def pour_in_cup(self):
        print 'pouring into cup'

    def customer_wants_condiments(self):
        return True


class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print 'dripping coffee through filter'

    def add_condiments(self):
        print 'adding sugar and milk'

    def customer_wants_condiments(self):
        answer = self.get_user_input()
        if answer.lower().startswith('y'):
            return True
        return False

    def get_user_input(self):
        answer = raw_input('would you like milk and sugar with your coffee (y/n)?')
        if not answer:
            return 'no'
        return answer


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print 'steeping the tea'

    def add_condiments(self):
        print 'adding lemon'

    def customer_wants_condiments(self):
        answer = self.get_user_input()
        if answer.lower().startswith('y'):
            return True
        return False

    def get_user_input(self):
        answer = raw_input('would you like lemon with your tea (y/n)?')
        if not answer:
            return 'no'
        return answer


if __name__ == '__main__':
    tea = TeaWithHook()
    coffee = CoffeeWithHook()

    print 'make tea...'
    tea.prepare_recipe()

    print 'make coffee'
    coffee.prepare_recipe()
