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


# Identify how the object you want to 'unpack' is structured.
# NC: is this how a standard HTML object is accessed???
def find_title():
    locator = 'article.product_pod h3 a'    # Set up CSS locator to access attrs
    return soup.select_one(locator).attrs['title']


def find_link():
    locator = 'article.product_pod h3 a'     # Set up CSS locator to access attrs
    return soup.select_one(locator).attrs['href']


# retrieve the price as a float.   Regex extracts split string bc float
# [^0-9\.] : xx . xx
def find_price():
    locator = 'article.product_pod div.product_price p.price_color'
    pattern = '£([0-9]+\.[0-9]+)'

    price = soup.select_one(locator).string
    matcher = re.search(pattern, price)
    return float(matcher.group(1))


def custom_filter(func, iterable):
    for i in iterable:
        if func(i) is True:
            yield i


def find_rating():
    locator = 'article.product_pod p.star-rating'
    rating = soup.select_one(locator)
    classes = rating.attrs['class']
    return list(custom_filter((lambda x: x != 'star-rating'), classes))[0]


soup = BeautifulSoup(ITEM_HTML, 'html.parser')

# Find the objects:
# title,
# link,
#obj_title = find_title()
#obj_link = find_link()
#float_price = find_price()
p(find_rating())

#p(obj_title)
#p(obj_link)
#p(float_price)




