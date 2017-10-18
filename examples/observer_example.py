#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 10:43
# @Author  : wangzz
# @File    : observer_example.py

import sys

sys.path.append('../design_patterns')

from design_patterns.observer import Subject, Observer, Observable


class WeatherData(Subject):
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print 'Current conditions: {} F degrees and {}% humidity'.format(self.temperature, self.humidity)


class StatisticsDisplay(Observer):
    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print 'Avg/Max/Min temperature = {}/{}/{}'.format(self.temperature - 5,
                                                          self.temperature,
                                                          self.temperature + 5)


class WeatherDataV2(Observable):
    def __init__(self):
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def measurements_changed(self):
        self.set_changed()
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure


class CurrentConditionsDisplayV2(Observer):
    def __init__(self, observable):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.observable = observable
        self.observable.add_observer(self)

    def update(self, observable, *args, **kwargs):
        if isinstance(observable, WeatherDataV2):
            self.temperature = observable.temperature
            self.humidity = observable.humidity
            self.display()

    def display(self):
        print 'Current conditions: {} F degrees and {}% humidity'.format(self.temperature, self.humidity)


if __name__ == '__main__':
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    weather_data.set_measurements(80, 65, 30.4)

    weather_data2 = WeatherDataV2()
    current_display2 = CurrentConditionsDisplayV2(weather_data2)
    weather_data2.set_measurements(80, 65, 30.4)
