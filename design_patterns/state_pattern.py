#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: state_pattern.py
@time: 2018/5/6
"""


# Context 是一个类，可以拥有一些内部状态
class Context(object):
    # 当 request() 被调用时，它就会被委托到状态来处理 state.handle()
    def request(self):
        pass


# State 接口定义了一个所有具体状态的共同接口，任何状态都实现这个相同的接口，
# 这样状态之间可以相互替换
class State(object):
    def handle(self):
        pass


# ConcreteState 具体状态处理来自 Context 的请求。
# 每一个 ConcreteState 都提供了它自己对于请求的实现。
# 当 Context 改变状态时行为也跟着改变。
class ConcreteStateA(State):
    def handle(self):
        pass


class ConcreteStateB(State):
    def handle(self):
        pass
