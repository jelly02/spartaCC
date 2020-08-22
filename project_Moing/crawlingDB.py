import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbmoing

# 크롤링 할 웹 사이트
# ages = [10, 20, 30, 40, 50, 60(부모님), 70(여자친구), 80(남자친구)]

# 1. 네이버
# ages[] = 10~50(url 파싱 가능) + 여친,남친,부모님,선생님 따로
# 2. 텐바이텐
# ages[] = 10,20,30(url 파싱 가능) + 여친,남친,부모님 따로


ages = [10, 20, 30, 40, 50, 60, 70]

# 1-남친 크롤링 정보 가져오기
def naver_bf():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A8%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&oquery=%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&tqi=UzBi4sp0JXVssNBQlMwssssst3N-151000',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    test = soup.select('div.group_guide >ul >li')
    # img alt:상품이름 , img src:이미지링크 , em title,em.text:가격

    for test2 in test:
        a_tag = test2.select_one('div>a')

        # print(name)
        if a_tag is not None:
            link = test2.select_one('a')['href']  # 상품 링크
            prdName = test2.select_one('img')['alt']  # 상품 이름
            prdImg = test2.select_one('img')['src']  # 상품 이미지
            prdPrice = test2.select_one('em')['title']  # 상품 가격
            print(link, "+", prdName, "+", prdImg, "+", prdPrice)




