import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://shoppinghow.kakao.com/search/10%EB%8C%80%20%EC%83%9D%EC%9D%BC%20%EC%84%A0%EB%AC%BC/sort_type:9&view_type:image&image_filter_cnt:200', headers=headers)

soup = BeautifulSoup(data.text,'html.parser')
print(soup)