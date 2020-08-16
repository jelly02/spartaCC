import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=10%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC', headers=headers)

soup = BeautifulSoup(data.text,'html.parser')

test = soup.select_one('#main_pack > div.sp_shop_default.section._shopping_guide_view > div.group_item > div.group_guide > div:nth-child(1) > div > ul > li:nth-child(1) > div > div.detail_area > div > div.tit > a')
test2 = soup.select('#main_pack > div.sp_shop_default.section._shopping_guide_view > div.group_item > div.group_guide > div:nth-child(1) > div > ul >li> div > div')
# print(test2)

# img alt:상품이름 , img src:이미지링크 , em title,em.text:가격

for test3 in test2:
    a_tag = test3.select_one('div > a')

    if a_tag is not None:
        prdName = test3.select_one('img')['alt'] #상품 이름
        prdImg = test3.select_one('img')['src'] #상품 이미지 width="133"
        # prdPrice = test3.select_one('em')['title'] 안됨

        print(prdName,prdImg) #네이버페이 플러스 https://ssl.pstatic.net/sstatic/search/pc/2016/img/ico_npay_plus3.png 가 같이 불러온다. 빼야하는데..

