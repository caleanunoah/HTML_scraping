import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint as p


class Locators:
    """
    Locators for items in the HTML page
    """
    CITY_LOCATOR = 'body div.'
    TEMP_LOCATOR = ''


def form_url(prov, city):
    pattern = '\s+'
    new_prov = re.sub(pattern, "-", prov)
    new_city = re.sub(pattern, "-", city)
    url = "https://www.theweathernetwork.com/ca/weather/" + new_prov.lower()+ "/" + new_city.lower()
    p(url)


def find_city():
    #locator = Locators.CITY_LOCATOR
    #city = soup.select_one(locator)
    #print(city)
    pass


#page = requests.get('https://www.theweathernetwork.com/ca')
#soup = BeautifulSoup(page.content, 'html.parser')
province = input('Enter a Canadian Province: ')
city = input("Enter a city in province: ")
form_url(province, city)







