#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wangzhizhao@zhihu.com
@file: pizza_factory_example.py
@time: 2017/11/19
"""


class Pizza(object):
    def __init__(self, name, dough, sauce, toppings):
        self._name = name
        self._dough = dough,
        self._sauce = sauce
        self._toppings = toppings

    @property
    def name(self):
        return self._name

    def prepare(self):
        print 'Preparing %s' % self._name
        print 'Tossing dough..'
        print 'Adding sauce...'
        print 'Adding toppings: '
        for topping in self._toppings:
            print '    %s' % topping

    def bake(self):
        print 'Bake for 25 minutes at 350'

    def cut(self):
        print 'Cutting the pizza into diagonal slices'

    def box(self):
        print 'Place pizza in official PizzaStore box'


class NYStoreCheesePizza(Pizza):
    def __init__(self):
        name = 'NY Style Sauce and Cheese Pizza'
        dough = 'Thin Cruse Dough'
        sauce = 'Marinara Sauce'
        toppings = ['Grated Reggiano Cheese']
        super(NYStoreCheesePizza, self).__init__(name, dough, sauce, toppings)


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        name = 'Chicago Style Deep Dish Cheese Pizza'
        dough = 'Extra Thick Crust Dough'
        sauce = 'Plum Tomato Sauce'
        toppings = ['Shredded Mozzarella Cheese']
        super(ChicagoStyleCheesePizza, self).__init__(name, dough, sauce, toppings)

    def cut(self):
        print 'Cutting the pizza into square slices'


class PizzaStore(object):
    def create_pizza(self, type):
        pass

    def order_pizza(self, type):
        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type):
        if type == 'cheese':
            pizza = NYStoreCheesePizza()
            return pizza
        else:
            raise ValueError('Type Not Supported')


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type):
        if type == 'cheese':
            pizza = ChicagoStyleCheesePizza()
            return pizza
        else:
            raise ValueError('Type Not Supported')


if __name__ == '__main__':
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza('cheese')
    print 'Ethan ordered a %s' % pizza.name

    pizza = chicago_store.order_pizza('cheese')
    print 'Joel ordered a %s' % pizza.name
