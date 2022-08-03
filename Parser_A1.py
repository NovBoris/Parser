# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.a1.by/ru/search?text=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%D1%8B'
# href = 1
# while True:
#     if href != 1:
#         url = 'https://www.a1.by/' + href
#     request = requests.get(url)
#     soup = BeautifulSoup(request.text, "html.parser")
#     teme = soup.find_all('div', class_="product-search-item-title")
#     mobile = []
#     for i in teme:
#         print(i.text)
#     try:
#         href = (soup.find('a', class_='link link--primary pagination-link icon icon--arrow-right')).get('href')
#     except AttributeError:
#         print('Товар закончился')
#         break
