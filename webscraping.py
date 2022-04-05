# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:42:21 2022

@author: ARMAN
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09976000000006&lon=-118.33197499999994#.YkyEHSgzaUl')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id = 'seven-day-forecast-body')
items = (week.find_all(class_ = 'tombstone-container'))
# print(items[0])
print(items[0].find(class_ = 'period-name').get_text())
print(items[0].find(class_ = 'short-desc').get_text())
print(items[0].find(class_ = 'temp').get_text())

period_names = [item.find(class_ = 'period-name').get_text() for item in items]
short_descriptions = [item.find(class_ = 'short-desc').get_text() for item in items]
tempatures = [item.find(class_ = 'temp').get_text() for item in items]
print(period_names)
print(short_descriptions)
print(tempatures)

weather_stuff = pd.DataFrame(
    {'period':period_names,
    'short_descriptions': short_descriptions,
    'tempatures': tempatures}
    )

print(weather_stuff)

weather_stuff.to_csv('weather.csv')

