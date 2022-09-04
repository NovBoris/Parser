import requests
from bs4 import BeautifulSoup
url = 'https://www.a1.by/ru/search?text=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%D1%8B'
href = 1
count = 1
mobile = []
prise_list = []
while True:
    if href != 1:
        url = 'https://www.a1.by/' + href
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    teme_phone = soup.find_all('div', class_="product-search-item-title")
    for i in teme_phone:
        mobile.append(i.text)
    teme_min_prise = soup.find_all('span', class_="price-value")
    print(f'Страница №{count}\n---------------------------------------')
    for i in teme_min_prise:
        prise_list.append(i.text.replace(u'\xa0', ''))
    try:
        href = (soup.find('a', class_='link link--primary pagination-link icon icon--arrow-right')).get('href')
    except AttributeError:
        print('Товар закончился')
        break
    count += 1

count = 0
for i in range(len(mobile)):
    print(f'Название телефона: {mobile[i]}\nЦена от {prise_list[count]} руб./мес - 24 мес'
          f'\nот {prise_list[count + 1]}')
    count += 2
