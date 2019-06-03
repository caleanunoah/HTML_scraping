import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint as p

page = requests.get('https://www.theweathernetwork.com/ca')
soup = BeautifulSoup(page.content, 'html.parser')
province = input('Enter a Canadian Province: ')
city = input("Enter a city in provinc: ")
adjust_prov(province)
url = "https://www.theweathernetwork.com/ca/weather/"+province+"/"+city
p(url)


#  Fix the province to account for strings with spaces.
#   Replace " " (spaces) with "-" (hyphens)
def fix_string(province):
    pass

class Locators:
    """
    Locators for items in the HTML page
    """
    CITY_LOCATOR = 'body div.'
    TEMP_LOCATOR = 'article.product_pod h3 a'


def find_city():
    locator = Locators.CITY_LOCATOR
    city = soup.select_one(locator)
    print(city)






