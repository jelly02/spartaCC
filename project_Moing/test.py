import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.shopping.naver.com/search/all?query=10%EB%8C%80%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&frm=NVSHATC&prevQuery=10%EB%8C%80%EC%84%A0%EB%AC%BC', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#__next > div > div.container > div > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child(1) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a
test = soup.select('#__next > div > div.container > div > div.style_content_wrap__1PzEo > div.style_content__2T20F')
#print(type(test)) > class 'bs4.element.ResultSet
#__next > div > div.container > div > div.style_content_wrap__1PzEo > div.style_content__2T20F > div.imgList_img_list__3-OHh > div > ul:nth-child(1) > li:nth-child(1) > div.imgList_info_area__-L6s4 > div.imgList_title__3yJlT > a
#__next > div > div.container > div > div.style_content_wrap__1PzEo > div.style_content__2T20F > div.imgList_img_list__3-OHh

#<물품 list의 물품 제목, 가격, 이미지 text 추출

#[방법 1] : X
# for prd in soup.find_all('a'):<a href="https://cr.shopping.naver.com/adcr.nhn?x=8lMXVzIDFKQ%2FIW9mXmXiMf%2F%2F…ftXaG%2BONdxJ%2BCqA6%2BrrPkSkQjk3bFq%2FUy&nvMid=82301749339&catId=50003353" target="_blank" class="basicList_link__1MaTN" rel="noopener" data-nclick="N=a:lst*N.title,i:82301749339,r:1" title="생일 케이크캔들 생일선물 이니셜케이크">생일 케이크캔들 생일선물 이니셜케이크</a>
#     print(prd.text.strip(),prd.get('title'))

#[방법 2] : X
# print(soup.find_all(attrs={'class':'div.imgList_img_list__3-OHh'}))

#[방법 3] : X
# for i in range(0,10):
#     print(soup.select('.div.imgList_img_list__3-OHh'[i].get_text()))

# [방법 4] : X
# test = soup.select('div.imgList_info_area__-L6s4')style_content__2T20F imgList_img_list__3-OHh

# [방법 5] : X
# new = soup.select('div.style_content_wrap__1PzEo > ul > li > a.title ')


