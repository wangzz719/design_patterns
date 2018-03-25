#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: facade_example.py
@time: 2018/3/25
"""

class DvdPlayer(object):
    def on(self):
        print 'dvd player on'

    def play(self, movie):
        print 'dvd play %s' % movie

    def eject(self):
        print 'dvd eject cd'

    def off(self):
        print 'dvd player off'

class Screen(object):
    def down(self):
        print 'screen down'
    def up(self):
        print 'screen off'

class HomeTheaterFacade():
    def __init__(self, dvd_player, screen):
        self._dvd_player = dvd_player
        self._screen = screen

    def watch_movie(self, movie):
        self._screen.down()
        self._dvd_player.on()
        self._dvd_player.play(movie)

    def end_movie(self):
        self._screen.up()
        self._dvd_player.eject()
        self._dvd_player.off()


if __name__ == '__main__':
    dvd_player = DvdPlayer()
    screen = Screen()
    home_theater = HomeTheaterFacade(dvd_player, screen)
    home_theater.watch_movie('Raiders of the Lost Ark')
    home_theater.end_movie()