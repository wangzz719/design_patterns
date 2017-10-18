#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 10:19
# @Author  : wangzz
# @File    : observer.py


class Subject(object):
    observers = []

    def register_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self):
        pass


class Observable(object):
    observers = []
    changed = False

    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        if self.changed:
            for observer in self.observers:
                observer.update(self, *args, **kwargs)

            self.changed = False

    def set_changed(self):
        self.changed = True


class Observer(object):
    def update(self, *args, **kwargs):
        pass
