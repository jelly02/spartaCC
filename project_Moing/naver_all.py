import requests
from bs4 import BeautifulSoup

ages = [10, 20, 30, 40, 50]

for age in ages:
    def naver_parse(url, age):
        url_forward = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='
        url_backword = '%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC'
        url = url_forward + age + url_backword

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url)
        soup = BeautifulSoup(data.text,'html.parser')
        items= soup.select('div.group_guide >ul >li')

        for item in items:
            a_tag= item.select_one('div>a')

            if a_tag is not None:
                link = item.select_one('a')['href'] #상품 링크
                prdName = item.select_one('img')['alt'] #상품 이름
                prdImg = item.select_one('img')['src'] #상품 이미지
                prdPrice = item.select_one('em')['title'] #상품 가격

                #print(link,"+",prdName,"+",prdImg,"+",prdPrice) (edited)