import requests
from bs4 import BeautifulSoup
url = 'https://nekdo.ru/short/'
href = 1
count = 1
while True:
    if href != 1:
        url = 'https://nekdo.ru' + href
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    teme = soup.find_all('div', class_="text")
    print(f'Страница № {count}\n------------------------')
    for i in teme:
        print(i.text, end='\n------------------------\n')
    try:
        href = (soup.find('a', class_='sel')).get('href')
    except AttributeError:
        print('Анекдоты все')
        break
    count += 1
