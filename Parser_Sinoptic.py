from bs4 import BeautifulSoup
import requests


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = response.text
    return html


def get_weather_now(text):
    url = f'https://sinoptik.ua/погода-{text.lower()}'
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        temp = soup.find('p', class_='today-temp').get_text(strip=True)
        description = soup.find('div', class_='description').get_text(strip=True)
        print(f'Температура воздуха сейчас {temp}\n{description}')
    except:
        print('Такого города нет')


while True:
    text = input('Введите город или stop: ')
    if text == 'stop':
        break
    get_weather_now(text)
    print()
