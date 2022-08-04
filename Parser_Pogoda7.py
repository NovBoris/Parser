# from bs4 import BeautifulSoup
# import requests
#
# while True:
#     url = 'https://pogoda7.ru/prognoz/BY-Belarus'
#     r = requests.get(url)
#     r.encoding = 'UTF-8'
#     soup = BeautifulSoup(r.text, 'html.parser')
#     teme = soup.find_all('a')
#     city = input('Введите город или Stop: ')
#     if city.capitalize() == 'Stop':
#         break
#     for i in teme:
#         if i.get_text().lower() == city.lower():
#             url = 'https://pogoda7.ru' + i.get('href')
#             r = requests.get(url)
#             r.encoding = 'UTF-8'
#             soup = BeautifulSoup(r.text, 'html.parser')
#             teme = soup.find('div', class_='temperature')
#             print(f'В городе {city.title()} сейчас {teme.text}')
#             break
#     else:
#         print('Такого города нет')
