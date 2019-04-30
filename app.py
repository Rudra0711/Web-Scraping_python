import htmlpage as HTML
from scraped import ParsedItems

#we can also pass a list of items of small contents of page for further analysis
#[ParsedItems(p) for p in soup.find)all('article')]
page=HTML.FIRST_PAGE

item=ParsedItems(page)

print(f"'{item.find_name()}' at {item.find_price()} rated at {item.find_rating()}")
