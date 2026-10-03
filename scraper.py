import requests
from selectolax.parser import HTMLParser
import pandas



def get_html(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    tree = HTMLParser(response.text)

    return tree


def collect_data(html):
    item_nodes = html.css('li.item.product.product-item')

    items = []

    for item_node in item_nodes:
        #urls
        item_url = item_node.css_first('div.product-item-inner a.product-item-link').attributes.get('href')

        #names
        item_name = item_node.css_first('div.product-item-inner > strong.product.name.product-item-name > a')

        #special price
        special_price = item_node.css_first('span.special-price span.price')

        #old price
        old_price = item_node.css_first('span.old-price span.price')

        item = {
        'item-name': item_name.text() if item_name is not None else None,
        'special-price': special_price.text() if special_price is not None else None,
        'old-price': old_price.text() if old_price is not None else None,
        'item-url': item_url
        
        }

        items.append(item)

    next_page = html.css_first('a.action.next')

    if next_page:
        next_url = next_page.attributes.get('href')
    else:
        next_url = None

    return items, next_url


url = 'https://www.shopkund.co.uk/men-s/kurta'
headers = {
    "User-Agent": "Mozilla/5.0"
}

all_items = []

while True:
    html = get_html(url, headers)
    items, next_url = collect_data(html)
    all_items.extend(items)

    if next_url:
        url = next_url
    else:
        break

df = pandas.DataFrame(all_items)
df.to_csv('products.csv', index=False)



