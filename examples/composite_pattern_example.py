#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: composite_pattern_example.py
@time: 2018/5/5
"""


class MenuComponent(object):
    def add(self, menu_component):
        raise Exception("Unsupported operation")

    def remove(self, menu_component):
        raise Exception("Unsupported operation")

    def get_child(self, i):
        raise Exception("Unsupported operation")

    def get_name(self):
        raise Exception("Unsupported operation")

    def get_description(self):
        raise Exception("Unsupported operation")

    def get_price(self):
        raise Exception("Unsupported operation")

    def is_vegetarian(self):
        raise Exception("Unsupported operation")

    def print_menu(self):
        raise Exception("Unsupported operation")


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def print_menu(self):
        s = " " + self.get_name()
        if self.is_vegetarian():
            s += "(v)"
        print "{}, {}    --- {}".format(s, self.get_price(), self.get_description())


class Menu(MenuComponent):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menu_components = []

    def add(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def get_child(self, i):
        return self.menu_components[i]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def print_menu(self):
        print '\n{}, {}--------------'.format(self.get_name(), self.get_description())
        for menu_component in self.menu_components:
            menu_component.print_menu()


class Waitress(object):
    def __init__(self, all_menus):
        self.all_menus = all_menus

    def print_menu(self):
        self.all_menus.print_menu()


if __name__ == '__main__':
    pancake_house_menu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    diner_menu = Menu("DINER MENU", "Lunch")
    cafe_menu = Menu("CAFE MENU", "Dinner")
    dessert_menu = Menu("DESSERT MENU", "Dessert of course!")

    all_menus = Menu("ALL MENUS", "All menus combined")

    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    diner_menu.add(MenuItem("Pasta", "Spaghetti with Marinara Sauce, and a slice of sourdough bread", True, 3.89))
    diner_menu.add(dessert_menu)

    dessert_menu.add(MenuItem("Apple Pie", "Apple pie with a flakey crust, topped with vanilla ice cream", True, 1.59))

    waitress = Waitress(all_menus)
    waitress.print_menu()
