# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 15:25
# @Author  : Sean
# @File    : 3_2_CityWeather.py

import requests
from collections import Iterable, Iterator

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

    def getWeather(self, city):
        r =requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s , %s ' % (city, data['low'], data['high'])

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable([u'北京', u'上海', u'广州', u'成都']):
    print(x)
