#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: command_pattern.py
@time: 2018/3/13
"""


# 命令对象接口，调用命令对象的 execute()方法可以让接受者进行相关的动作
class Command(object):

    def execute(self):
        pass

    def undo(self):
        pass


# 接受者是实际执行操作的对象
class Receiver(object):
    def action(self):
        pass


# 调用者持有命令对象，调用命令对象的 execute() 或 undo() 方法来执行或取消一个操作
class Invoker(object):
    def setCommand(self):
        pass
