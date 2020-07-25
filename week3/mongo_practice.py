import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

soup = BeautifulSoup(data.text, "html.parser")
movies = soup.select("#old_content > table > tbody > tr")

for movie in movies:
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None: # None이 없을 때 예외처리
        rank = movie.select_one('td:nth-child(1) > img')["alt"]
        title = movie.select_one('td.title > div > a')["title"]
        point = movie.select_one('td.point').text
        movie = {'rank': rank, 'title': title, 'point': point}
        db.users.insert_one(movie)