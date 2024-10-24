import os
import requests
from bs4 import BeautifulSoup

def get_product_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', class_='item')  # Adjust the class name based on the website structure
    product_list = []
    for product in products:
        product_info = {
            'name': product.find('h3', class_='title').text.strip(),
            'price': product.find('span', class_='price').text.strip(),
            'description': product.find('p', class_='desc').text.strip()
        }
        product_list.append(product_info)
    return product_list

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

categories = {
    'Backpacks': 'https://s.1688.com/selloffer/offer_search.htm?keywords=backpacks&spm=a26352.13672862.searchbox.0',
    'Electronics': 'https://s.1688.com/selloffer/offer_search.htm?keywords=Electronics&spm=a26352.13672862.searchbox.0',  # Replace with actual URL
    'Clothing': 'https://s.1688.com/selloffer/offer_search.htm?keywords=Clothing&spm=a26352.13672862.searchbox.0'  # Replace with actual URL
}

for category, url in categories.items():
    products = get_product_data(url)
    save_products_to_file(category, products)
