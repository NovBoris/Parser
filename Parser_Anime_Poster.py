import requests
from bs4 import BeautifulSoup
url = 'https://animego.org/'
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
teme_1 = soup.find_all('span', class_='last-update-title font-weight-600')
anime = []
for i in teme_1:
    anime.append(i.get_text(strip=True))
teme_2 = soup.find_all('div', class_='font-weight-600 text-truncate')
series = []
for i in teme_2:
    series.append(i.get_text(strip=True))
teme_3 = soup.find_all('div', class_='text-gray-dark-6')
voice_acting = []
for i in teme_3:
    voice_acting.append(i.get_text(strip=True))
anime_updates = {}
anime_schedule = {}
for i in range(len(anime)):
    if voice_acting[i][1:3].strip().isdigit():
        if anime[i].lower() not in anime_schedule:
            anime_schedule[anime[i].lower()] = [series[i] + ' ' + voice_acting[i]]
        else:
            anime_schedule[anime[i].lower()] += [series[i] + ' ' + voice_acting[i]]
    else:
        if anime[i].lower() not in anime_updates:
            anime_updates[anime[i].lower()] = [series[i] + ' ' + voice_acting[i]]
        else:
            anime_updates[anime[i].lower()] += [series[i] + ' ' + voice_acting[i]]
print(anime_updates)
for k, v in anime_schedule.items():
    print(f'{k}: {v}')
