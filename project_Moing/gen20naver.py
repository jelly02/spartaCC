import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=20%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&oquery=10%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&tqi=UzBnbsp0J1ZssuWvfCRssssstkC-301226', headers=headers)

soup = BeautifulSoup(data.text,'html.parser')
test = soup.select('div.group_guide >ul >li')
# print(test)

# img alt:상품이름, img src:상품 이미지,

for test2 in test:
    a_tag= test2.select_one('div>a')
    name = test2.select_one('a')['href']
    # print(name)
    if a_tag is not None:
        prdName = test2.select_one('img')['alt'] #상품 이름
        prdImg = test2.select_one('img')['src'] #상품 이미지
        print(prdImg,prdName)