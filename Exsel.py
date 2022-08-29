from bs4 import BeautifulSoup
import requests
import pandas

url = 'https://www.wildberries.by/catalog/elektronika/igry-i-razvlecheniya/aksessuary/garnitury'


r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
teme = soup.find_all('span', class_='goods-name')
print(teme)
for i in teme:
    print(i.text)


