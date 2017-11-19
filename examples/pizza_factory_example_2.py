#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: pizza_factory_example_2.py
@time: 2017/11/19
"""


class PizzaIngredientFactory(object):
    def create_dough(self):
        pass

    def create_sauce(self):
        pass

    def create_cheese(self):
        pass

    def create_veggies(self):
        pass

    def create_pepperoni(self):
        pass

    def create_calm(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return 'Thin Crust Dough'

    def create_sauce(self):
        return 'Marinara Sauce'

    def create_cheese(self):
        return 'Reggiano Cheese'

    def create_veggies(self):
        return ['Garlic', 'Onion', 'Mushroom', 'RedPepper']

    def create_pepperoni(self):
        return 'Sliced Pepperoni'

    def create_clam(self):
        return 'Fresh Calms'


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return 'Thick Crust Dough'

    def create_sauce(self):
        return 'Plum Tomato Sauce'

    def create_cheese(self):
        return 'Shredded Mozzarella Cheese'

    def create_veggies(self):
        return ['Garlic', 'Onion', 'Mushroom', 'RedPepper']

    def create_pepperoni(self):
        return 'Sliced Pepperoni'

    def create_clam(self):
        return 'Fresh Clams'


class Pizza(object):
    def __init__(self, name=None, dough=None, sauce=None, veggies=None, cheese=None, pepperoni=None, clam=None):
        self._name = name
        self._dough = dough,
        self._sauce = sauce
        self._veggies = veggies
        self._cheese = cheese
        self._pepperoni = pepperoni
        self._clam = clam

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def prepare(self):
        pass

    def bake(self):
        print 'Bake for 25 minutes at 350'

    def cut(self):
        print 'Cutting the pizza into diagonal slices'

    def box(self):
        print 'Place pizza in official PizzaStore box'

    def __str__(self):
        return 'Pizza: %s' % self._name


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self._ingredient_factory = ingredient_factory
        dough = ingredient_factory.create_dough()
        sauce = ingredient_factory.create_sauce()
        cheese = ingredient_factory.create_cheese()
        super(CheesePizza, self).__init__(dough=dough, sauce=sauce, cheese=cheese)

    def prepare(self):
        print self._name


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        self._ingredient_factory = ingredient_factory

        super(ClamPizza, self).__init__()

    def prepare(self):
        print self._name
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._clam = self._ingredient_factory.create_clam()


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
    def create_pizza(self, item):
        ingredient_factory = NYPizzaIngredientFactory()
        if item == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.name = 'New York Style Cheese Pizza'
        elif item == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.name = 'New York Style Clam Pizza'
        else:
            raise ValueError('Type Not Supported')
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, item):
        ingredient_factory = ChicagoPizzaIngredientFactory()
        if item == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.name = 'Chicago Style Cheese Pizza'
        elif item == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.name = 'Chicago Style Clam Pizza'
        else:
            raise ValueError('Type Not Supported')
        return pizza


if __name__ == '__main__':
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza('cheese')
    print 'Ethan ordered a %s' % pizza.name

    pizza = chicago_store.order_pizza('cheese')
    print 'Joel ordered a %s' % pizza.name
