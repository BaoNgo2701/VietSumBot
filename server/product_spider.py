import scrapy
import os
import requests
from bs4 import BeautifulSoup

class ProductSpider(scrapy.Spider):
    name = "product_spider"
    start_urls = [
        'https://s.1688.com/selloffer/offer_search.htm?keywords=backpack&spm=a26352.13672862.searchbox.0',
        'https://s.1688.com/selloffer/offer_search.htm?keywords=clothing&spm=a260k.home2024.searchbox.0',
        'https://s.1688.com/selloffer/offer_search.htm?keywords=stationery&spm=a260k.home2024.searchbox.0'
    ]

    def parse(self, response):
        for product_link in response.css('a.search-offer-wrapper::attr(href)').getall():
            yield response.follow(product_link, self.parse_product)

    def parse_product(self, response):
        product_info = {
            'name': response.css('div.offer-title-row .title-text div::text').get().strip(),
            'price': ''.join(response.css('div.price-units::text').get().strip() +
                             response.css('div.text-main::text').get().strip()),
            'description': ' '.join([desc.strip() for desc in response.css('div.offer-desc-row .desc-text::text').getall()])
        }
        yield product_info

def save_products_to_file(category, products):
    base_path = f'server/product_data/{category}'
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    for i, product in enumerate(products):
        file_path = os.path.join(base_path, f'product_{i}.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Name: {product['name']}\n")
            file.write(f"Price: {product['price']}\n")
            file.write(f"Description: {product['description']}\n")
