import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.shopping.naver.com/search/all?query=10%EB%8C%80%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&frm=NVSHATC&prevQuery=10%EB%8C%80%EC%84%A0%EB%AC%BC', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

test = soup.select('#__next > div > div.container > div > div.style_content_wrap__1PzEo > div.style_content__2T20F')
#print(type(test)) > class 'bs4.element.ResultSet

#__next > div > div.container > div > div.style_content_wrap__1PzEo > div.style_content__2T20F > div.imgList_img_list__3-OHh
# 물품 리스트가 있는 div 이름 : div.imgList_img_list__3-OHh
# 물품 정보가 있는 li 한 개 이름 : imgList_list_item__226HB

#<물품 list의 물품 제목, 가격, 이미지 text 추출

#[방법 1] : X
# for prd in soup.find_all('a'):
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


