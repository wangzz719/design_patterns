#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: state_pattern_example.py
@time: 2018/5/6
"""


class State(object):
    def insert_quarter(self):
        pass

    def eject_quarter(self):
        pass

    def turn_crank(self):
        pass

    def dispense(self):
        pass


class GumballMachine(object):
    def __init__(self, number_gumballs):
        self._count = number_gumballs
        self._no_quarter_state = NoQuarterState(self)
        self._has_quarter_state = HasQuarterState(self)
        self._sold_state = SoldState(self)
        self._sold_out_state = SoldOutState(self)
        self._state = self._sold_out_state
        if self._count > 0:
            self._state = self._no_quarter_state

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, number_gumballs):
        self._count = number_gumballs

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state

    @property
    def no_quarter_state(self):
        return self._no_quarter_state

    @no_quarter_state.setter
    def no_quarter_state(self, state):
        self._no_quarter_state = state

    @property
    def has_quarter_state(self):
        return self._has_quarter_state

    @has_quarter_state.setter
    def has_quarter_state(self, state):
        self._has_quarter_state = state

    @property
    def sold_state(self):
        return self._sold_state

    @sold_state.setter
    def sold_state(self, state):
        self._sold_state = state

    @property
    def sold_out_state(self):
        return self._sold_out_state

    @sold_out_state.setter
    def sold_out_state(self, state):
        self._sold_out_state = state

    def release_ball(self):
        print "A gumball comes rolling out the slot..."
        if self.count != 0:
            self.count -= 1

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()


class NoQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print "You inserted a quarter"
        self.gumball_machine.state = self.gumball_machine.has_quarter_state

    def eject_quarter(self):
        print "You haven't insert a quarter"

    def turn_crank(self):
        print "You haven't insert a quarter"

    def dispense(self):
        print "You need to pay first"


class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print "You can't inserted another quarter"

    def eject_quarter(self):
        print "Quarter returned"
        self.gumball_machine.state = self.gumball_machine.no_quarter_state

    def turn_crank(self):
        print "You turned..."
        self.gumball_machine.state = self.gumball_machine.sold_state

    def dispense(self):
        print "No gumball dispensed"


class SoldState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print "Please wait, we're already giving you a gumball"

    def eject_quarter(self):
        print "Sorry, you already turned the crank"

    def turn_crank(self):
        print "Turning twice doesn't give you another gumball"

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.count > 0:
            self.gumball_machine.state = self.gumball_machine.no_quarter_state
        else:
            print "Oops, out of gumballsQ"
            self.gumball_machine.state = self.gumball_machine.sold_out_state


class SoldOutState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print "You can't insert a quarter, the machine is sold out"

    def eject_quarter(self):
        print "You can't eject, you haven't inserted a quarter"

    def turn_crank(self):
        print "You turned, but there are no gumballs"

    def dispense(self):
        print "No gumball dispensed"


if __name__ == '__main__':
    gumball_machine = GumballMachine(5)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    gumball_machine.insert_quarter()
    gumball_machine.insert_quarter()
    gumball_machine.eject_quarter()
    gumball_machine.turn_crank()

    gumball_machine.insert_quarter()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.eject_quarter()

