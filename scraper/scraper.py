import requests
from lxml import html

def scrape_page(url):
    content = requests.get(url).content
    return process(content)

def process(html_string):
    html_tree = html.fromstring(html_string)
    listings = html_tree.xpath('//div[contains(@class, "vehicle-details")]')
    for listing in listings:
        badge_label_span = listing.xpath('.//span[contains(@class, "sds-badge__label")]')
        mileage_div = listing.xpath('.//div[contains(@class, "mileage")]')
        link = listing.xpath('.//a[@href]')
        price_span = listing.xpath('.//span[contains(@class, "primary-price")]')
        mileage = mileage_div[0].text.strip() if mileage_div else 'N/A'
        listing_link = 'https://www.cars.com' + link[0].get('href') if link else 'N/A'
        price = price_span[0].text.strip() if price_span else 'N/A'
        badge_label = badge_label_span[0].text.strip() if badge_label_span else 'N/A'
        print("Listing Found:")
        print("Mileage:", mileage)
        print("Link:", listing_link)
        print("Price:", price)
        print("Badge Label:", badge_label)
        print('-----')

url = 'https://www.cars.com/shopping/results/?stock_type=used&makes%5B%5D=mazda&models%5B%5D=mazda-cx_5&list_price_max=15000&maximum_distance=100&zip=30064'

scrape_page(url)