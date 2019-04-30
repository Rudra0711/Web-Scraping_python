import locator as ParsedItemsLocator
from bs4 import BeautifulSoup
import htmlpage as HTML

class ParsedItems:

    """
        A class which will take html page and return parsed contents of it
    """

    def __init__(self,page):
        self.soup=BeautifulSoup(page,'html.parser')

    def find_name(self):
        locator=ParsedItemsLocator.NAME_LOCATOR
        title=self.soup.select_one(locator).attrs['title']
        return(f"{title}")

    def find_rating(self):
        locator=ParsedItemsLocator.RATING_LOCATOR
        rating=self.soup.select_one(locator).attrs['class']
        stars=[stars for stars in rating if stars!='star-rating']
        return(f"{stars[0]} stars")

    def find_price(self):
        locator=ParsedItemsLocator.PRICE_LOCATOR
        price=self.soup.select_one(locator).string[1:]
        return(f"${price}")
