import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EB%AA%A8%EB%8B%98+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&oquery=50%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&tqi=UzBiswp0J14ssj1LkZlssssstKN-072912', headers=headers)

soup = BeautifulSoup(data.text,'html.parser')

# test = soup.select_one('#main_pack > div.sp_shop_default.section._shopping_guide_view > div.group_item > div.group_guide > div:nth-child(1) > div > ul > li:nth-child(1) > div > div.detail_area > div > div.tit > a')
# test2 = soup.select('#main_pack > div.sp_shop_default.section._shopping_guide_view > div.group_item > div.group_guide > div:nth-child(1) > div > ul >li> div > div')
test= soup.select('div.group_guide >ul >li')
# img alt:상품이름 , img src:이미지링크 , em title,em.text:가격
#### 보류

for test2 in test:
    a_tag= test2.select_one('div>a')

    # print(name)
    if a_tag is not None:
        link = test2.select_one('a')['href'] #상품 링크
        prdName = test2.select_one('img')['alt'] #상품 이름
        prdImg = test2.select_one('img')['src'] #상품 이미지
        # prdPrice = test2.select_one('em')['title'] #상품 가격
        print(link,"+",prdName,"+",prdImg,"+")