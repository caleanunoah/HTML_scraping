from bs4 import BeautifulSoup
from pprint import pprint as p
import re

ITEM_HTML = '''<html>
<head></head>

<body>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
        <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                 <i class="icon-star"></i>
                 <i class="icon-star"></i>
                 <i class="icon-star"></i>
                 <i class="icon-star"></i>
                 <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>

            <div class="product_price">
             <p class="price_color">£51.77</p>
             <p class="instock availability">
                <i class="icon-ok"></i>
                In stock    </p>
                <form>
                <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                </form>
            </div>  

    </article>
</li>
</body></html>  '''


class Locators:
    """
    Locators for items in the HTML page
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod div.product_price p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:
    """
    Take in an HTML page (or sections) and find properties of it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def title(self):
        locator = Locators.NAME_LOCATOR  # Set up CSS locator to access attrs
        return self.soup.select_one(locator).attrs['title']

    @property
    def link(self):
        locator = Locators.LINK_LOCATOR  # Set up CSS locator to access attrs
        return self.soup.select_one(locator).attrs['href']

    @property
    def price(self):
        locator = Locators.PRICE_LOCATOR
        pattern = '£([0-9]+\.[0-9]+)'  # retrieve the price as a float: xx.xx
        price = self.soup.select_one(locator).string
        matcher = re.search(pattern, price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = Locators.RATING_LOCATOR
        rating = self.soup.select_one(locator)
        classes = rating.attrs['class']
        return list(filter((lambda x: x != 'star-rating'), classes))[0]


item = ParsedItem(ITEM_HTML)
print(item.title)
print(item.link)
print(item.price)
print(item.rating)




