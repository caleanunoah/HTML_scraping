import requests
import re

from bs4 import BeautifulSoup
from pprint import pprint as p


#  Fix the province to account for strings with spaces.
#   Replace " " (spaces) with "-" (hyphens)
def fix_strings(province, city):
    pattern = '\s'
    adj_prov = re.sub(pattern, '-', province)
    adj_city = re.sub(pattern, '-', city)
    url = "https://www.theweathernetwork.com/ca/weather/"+adj_prov.lower()+"/"+adj_city.lower()
    p(url)
    return url


class Locators:
    """
    Locators for items in the HTML page
    """
    CITY_LOCATOR = 'body'
    #TEMP_LOCATOR = 'body div.content-wrap div.clearfix div.o-main-content div.module div.wx-content.current-obs div.current-wx-obs.override-margin div.wx-info_card div.obs-area span.temp'
    TEMP_LOCATOR = 'body div.content-wrap div.clearfix div.o-main-content'


class WeatherPage:
    """
    This returns the container where all weather info is extracted from.
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'lxml')

    def weather(self):
        locator = Locators.TEMP_LOCATOR
        #city = self.soup.select(locator)
        data= self.soup.find("span", attrs={"class": "wxcondition", })
        return data[0]
        #return self.soup.select_one(locator).prettify()
        #return self.soup.select_one(locator)
        #return WeatherParser(city)

'''
class WeatherParser:
"""

"""
    def __init__(self, parent):
        self.parent = parent            # THIS IS NONE

    def __repr__(self):
        return f'<The weather in {self.parent} is X'    # PRINTS EMPTY LIST BC PARENT IS NONE!!!!

    @property
    def temp(self):
        temp_locator = Locators.TEMP_LOCATOR
        return self.parent.select_one(temp_locator)
'''

if __name__ == '__main__':
    #province = input('Enter a Canadian province: ')
    #City = input("Enter a city in province: ")
    #URL = fix_strings(province, City)
    URL = 'https://www.theweathernetwork.com/ca/36-hour-weather-forecast/british-columbia/surrey'
    page_content = requests.get(URL).content
    Weather = WeatherPage(page_content)
    p("Im done scraping. ")
    p(Weather.weather())
    #locator = Locators.CITY_LOCATOR
    #city = soup.select_one(locator)







