#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: command_pattern_example.py
@time: 2018/3/13
"""


class Command(object):
    def execute(self):
        pass

    def undo(self):
        pass


class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()


class TVOnCommand(Command):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.on()

    def undo(self):
        self._tv.off()


class TVOffCommand(Command):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.off()

    def undo(self):
        self._tv.on()


class Light(object):
    def on(self):
        print "light on"

    def off(self):
        print "light off"


class TV(object):
    def on(self):
        print "tv on"

    def off(self):
        print "tv off"


class MarcoCommand(object):
    def __init__(self, commands):
        self._commands = commands

    def execute(self):
        for command in self._commands:
            command.execute()

    def undo(self):
        for command in self._commands:
            command.undo()


class RemoteControl(object):
    undo_commands = None
    on_commands = []
    off_commands = []

    def __init__(self):
        self.undo_command = NoCommand()
        for i in xrange(4):
            self.on_commands.append(NoCommand())
            self.off_commands.append(NoCommand())

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pushed(self, slot):
        self.undo_command = self.on_commands[slot]
        self.on_commands[slot].execute()

    def off_button_pushed(self, slot):
        self.undo_command = self.off_commands[slot]
        self.off_commands[slot].execute()

    def undo_button_pushed(self):
        self.undo_command.undo()

    def __str__(self):
        str = ""
        for i in xrange(len(self.on_commands)):
            str += "slot[{}] {} {}\n".format(i, self.on_commands[i].__class__.__name__,
                                           self.off_commands[i].__class__.__name__)

        return str

if __name__ == '__main__':
    light = Light()
    tv = TV()

    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    tv_on_command = TVOnCommand(tv)
    tv_off_command = TVOffCommand(tv)

    remote_control = RemoteControl()
    remote_control.set_command(0, light_on_command, light_off_command)
    remote_control.set_command(1, tv_on_command, tv_off_command)

    marco_on_command = MarcoCommand([light_on_command, tv_on_command])
    marco_off_command = MarcoCommand([light_off_command, tv_off_command])

    remote_control.set_command(2, marco_on_command, marco_off_command)

    print remote_control

    print '-----'
    remote_control.on_button_pushed(0)
    remote_control.on_button_pushed(1)
    print '-----'
    remote_control.off_button_pushed(1)
    remote_control.off_button_pushed(0)
    print '-----'
    remote_control.on_button_pushed(2)
    remote_control.off_button_pushed(2)
    print '-----'
    remote_control.undo_button_pushed()
