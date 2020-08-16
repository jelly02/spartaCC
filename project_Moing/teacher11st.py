import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://search.11st.co.kr/Search.tmall?kwd=%25EC%258A%25A4%25EC%258A%25B9%25EC%259D%2598%25EB%2582%25A0%2520%25EC%2584%25A0%25EB%25AC%25BC', headers=headers)

soup = BeautifulSoup(data.text,'html.parser')

test=soup.select_one('#contsWrap > div > section:nth-child(3) > ul >li')
print(test)
