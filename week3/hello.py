import requests
from bs4 import BeautifulSoup

# 요청을 보낼 때
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# 해당 HTML 홈페이지 태그를 다 가져옴
soup = BeautifulSoup(data.text, "html.parser")

# select() : selector를 가져오는 메소드, 모든 결과를 리스트에 담음
movies = soup.select("#old_content > table > tbody > tr")

# select_one() : 하나의 요소만 반환 * movies[0]은 구분선 *
#print(movies[1].select_one('td.title > div > a'))

# title = '' : 이 내용을 가져옴
#print(movies[1].select_one('td.title > div > a')["title"])

# text : tag 안 내용을 가져옴
# print(movies[1].select_one('td.title > div > a'.text))

# movies의 길이만큼 도는 반복문
# for i in range(len(movies)) :


for movie in movies:
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None: # None이 없을 때 예외처리
        rank = movie.select_one('td:nth-child(1) > img')["alt"]
        title = movie.select_one('td.title > div > a')["title"]
        # print(movie.select_one('td.title > div > a').text)
        point = movie.select_one('td.point').text
        print(rank,title,point)
