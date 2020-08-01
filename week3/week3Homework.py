import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)

soup = BeautifulSoup(data.text, "html.parser")
box = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

# print(box)

for music_list in box:
    rank = box.select_one('td.number').text
    title = box.select_one('td.info > a.title.ellipsis').text
    name = box.select_one('td.info > a.artist.ellipsis').text
    print(rank,title,name)

# for music_list in box:
#     rank = soup.find('td', {'class': 'number'}).text
#     title = soup.find('a', {'class': 'title ellipsis'}).text
#     name = soup.find('a', {'class': 'artist ellipsis'}).text
#     print(rank, title, name)