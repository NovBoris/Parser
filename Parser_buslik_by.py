from math import floor
from bs4 import BeautifulSoup
import requests


def product_page_parsing(href: str) -> str:
    r = requests.get('https://buslik.by' + href)
    r.encoding = 'UTF-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    teme = soup.find('div', class_='product-action__price-current').get_text(strip=True)
    return teme


def href_parsing(url: str, page: int) -> str:
    r = requests.get(url)
    r.encoding = 'UTF-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    href = soup.find_all('a', class_='new-pagination__link')
    for i in href:
        if i.text == str(page):
            href = i.get('href')
            print(href)
            return href
    else:
        print('Товар закончился')
        href = None
        return href


url = 'https://buslik.by/catalog/podguzniki/podguzniki_1/'
page = 1
while True:
    if page != 1:
        href = href_parsing(url, page)
        if href == None:
            break
        url = 'https://buslik.by' + href
        print(url)
    r = requests.get(url)
    r.encoding = 'UTF-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    teme = soup.find_all('a', class_='catalog-item__link')
    for i in teme:
        print(product_page_parsing(i.get('href')))
    page += 1

url = 'https://buslik.by/catalog/podguzniki/podguzniki_1/'
page = 2
price_list = []
title_list = []
item_discount_list = []
while True:
    if page != 2:
        url = 'https://buslik.by' + href
    r = requests.get(url)
    r.encoding = 'UTF-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    teme_catalog_item__prices = soup.find_all('div', class_='catalog-item__prices')
    for i in teme_catalog_item__prices:
        price_list.append((i.get_text(strip=True)).split(' руб.'))
    teme_title = soup.find_all('a', class_='catalog-item__name')
    for i in teme_title:
        title_list.append(i.get_text(strip=True))
    href = soup.find_all('a', class_='new-pagination__link')
    for i in href:
        if i.text == str(page):
            href = i.get('href')
            break
    else:
        break
    page += 1
result = dict(zip(title_list, price_list))
id = 1
for k, v in result.items():
    print(f'{id}. Наименование: {k}\nЦена: {v[0]} руб.' if v[1] == ''
          else f'{id}. Наименование: {k}\nЦена: {v[0]} руб. Старая цена {v[1]} руб. Скидка: '
               f'{floor(((float(v[1]) - float(v[0])) / float(v[1])) * 100)} %')
    id += 1
