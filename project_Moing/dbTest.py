from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.moing

# age[] = 10, 20, 30, 40, 50, 60(여자친구), 70(남자친구), 80(부모님)
# 1. 네이버 : 10~50번 까지 url 파싱 가능, 60,70,80 따로 만들어야 함
# 2. 텐바이텐 : 10~30번 까지 url 파싱 가능, 60,70,80 따로 만들어야 함

# def mysite1() :
#     return list  > 크롤링하는 함수 한 개에서 list를 리턴,
#                    이렇게 크롤링 list1,2,3,4가 쌓이면
# for item in list1 :
#    db.collection1.insert_one(item) > 리스트 한 개에 있는 값 다 빼오고 나머지 반복
#                                      데이터가 중복으로 들어가는 게 싫으면 collection을 삭제

# <로직 설명>
# 1. 사용자가 프론트에서 검색 하고 싶은 연령대 (user_num)값을 넘기면
# 2. 그 값을 받아 DB genList 테이블 find(genNum:user_num)으로 찾아서
# 3. 해당 연령대 선물 리스트를 return
# 4. 프론트에서 CARD for문으로 돌려서 출력

# 1-1. 네이버 10~50대 크롤링

ages = [10, 20, 30, 40, 50]
# print(ages)
naver10to50_total = []

def naver10to50Url(age):
    temp_list = []
    temp_list.append(age)

    url_forward = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='
    url_backword = '%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC'
    url = url_forward + str(age) + url_backword
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    items = soup.select('div.group_guide >ul >li')
    for item in items:
        a_tag = item.select_one('div>a')
        if a_tag is not None:
            link = item.select_one('a')['href']  # 상품 링크
            prdName = item.select_one('img')['alt']  # 상품 이름
            prdImg = item.select_one('img')['src']  # 상품 이미지
            prdPrice = item.select_one('em')['title']  # 상품 가격
            # print(link,"+",prdName,"+",prdImg,"+",prdPrice)
            str_age = str(age)
            prdList = {
                'genCode': str_age,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }

            # print(type(age), type(link))
            db.HapB.insert_one(prdList)

# for age in ages:
#     naver10to50Url(age)


# 1-2. 네이버 여자친구 크롤링 0
def naverGfUrl():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&oquery=%EB%B6%80%EB%AA%A8%EB%8B%98+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&tqi=UzBiZwp0Jy0ssi4JRPsssssstPd-419548',
        headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    items = soup.select('div.group_guide >ul >li')
    # img alt:상품이름 , img src:이미지링크 , em title,em.text:가격
    genCode = 60;

    for item in items:
        a_tag = item.select_one('div>a')

        # print(name)
        if a_tag is not None:
            # genCode
            link = item.select_one('a')['href']  # 상품 링크
            prdName = item.select_one('img')['alt']  # 상품 이름
            prdImg = item.select_one('img')['src']  # 상품 이미지
            prdPrice = item.select_one('em')['title']  # 상품 가격
            # print(genCode,"+",link, "+", prdName, "+", prdImg, "+", prdPrice)

            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }

            db.HapB.insert_one(prdList)
    print('네이버 여자친구 크롤링 저장 완료!')


# naverGfUrl()

# 1-3. 네이버 남자친구 크롤링
def naverBfUrl():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A8%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&oquery=%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&tqi=UzBi4sp0JXVssNBQlMwssssst3N-151000',
        headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    items = soup.select('div.group_guide >ul >li')
    genCode = 70;

    for item in items:
        a_tag = item.select_one('div>a')

        # print(name)
        if a_tag is not None:
            genCode
            link = item.select_one('a')['href']  # 상품 링크
            prdName = item.select_one('img')['alt']  # 상품 이름
            prdImg = item.select_one('img')['src']  # 상품 이미지
            prdPrice = item.select_one('em')['title']  # 상품 가격
            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('네이버 남자친구 크롤링 저장 완료!')


# 1-4. 텐바이텐 10대~30대 크롤링

ages = [10, 20, 30]
txt10to30_total = []

def txt10to30Url(age):
    temp_list = []
    temp_list.append(age)

    url_forward = 'http://www.10x10.co.kr/search/search_result.asp?rect='
    url_backword = '%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&exkw=1'
    url = url_forward + str(age) + url_backword
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    items = soup.select('div.pdtWrap>ul>li ')

    for item in items:
        a_tag = item.select_one('div>a')
        price_tag = item.select_one('div>div>p>span')

        if a_tag is not None:
            link = "http://www.10x10.co.kr" + item.select_one('a')['href']  # 상품 링크
            prdName = item.select_one('img')['alt']  # 상품 이름
            prdImg = item.select_one('img')['src']  # 상품 이미지
            prdPrice = price_tag.text  # 상품 가격

            str_age = str(age)
            prdList = {
                'genCode': str_age,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            print(prdList)
            # print(type(age), type(link))
            db.HapB.insert_one(prdList)
#
# for age in ages:
#     txt10to30Url(age)


# 1-5. 텐바이텐 여자친구 크롤링
def txtGfUrl():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'http://www.10x10.co.kr/search/search_result.asp?rect=%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%84%A0%EB%AC%BC&prvtxt=%EC%97%84%EB%A7%88+%EC%84%A0%EB%AC%BC&rstxt=%EC%97%84%EB%A7%88+%EC%84%A0%EB%AC%BC&extxt=&sflag=&dispCate=&cpg=1&chkr=False&chke=False&mkr=&sscp=N&psz=60&srm=be&iccd=&styleCd=&attribCd=&icoSize=M&arrCate=&deliType=&minPrc=&maxPrc=&lstDiv=search&subshopcd=&giftdiv=&prectcnt=869',
        headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    items = soup.select('div.pdtWrap>ul>li ')
    genCode = 60;

    for item in items:
        a_tag = item.select_one('div>a')
        price_tag = item.select_one('div>div>p>span')

        if a_tag is not None:
            genCode
            link = "http://www.10x10.co.kr" + item.select_one('a')['href']  # 상품 링크
            prdName = item.select_one('img')['alt']  # 상품 이름
            prdImg = item.select_one('img')['src']  # 상품 이미지
            prdPrice = price_tag.text  # 상품 가격
            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('텐바이텐 여자친구 크롤링 저장 완료!')


# 1-6. 텐바이텐 남자친구 크롤링
def txtBfUrl():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'http://www.10x10.co.kr/search/search_result.asp?rect=%EB%82%A8%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%84%A0%EB%AC%BC&prvtxt=%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%84%A0%EB%AC%BC&rstxt=%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%84%A0%EB%AC%BC&extxt=&sflag=&dispCate=&cpg=1&chkr=False&chke=False&mkr=&sscp=N&psz=60&srm=be&iccd=&styleCd=&attribCd=&icoSize=M&arrCate=&deliType=&minPrc=&maxPrc=&lstDiv=search&subshopcd=&giftdiv=&prectcnt=7268',
        headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    items = soup.select('div.pdtWrap>ul>li ')
    genCode = 70;

    for item in items:
        a_tag = item.select_one('div>a')
        price_tag = item.select_one('div>div>p>span')

        if a_tag is not None:
            genCode
            link = "http://www.10x10.co.kr" + item.select_one('a')['href']  # 상품 링크
            prdName = item.select_one('img')['alt']  # 상품 이름
            prdImg = item.select_one('img')['src']  # 상품 이미지
            prdPrice = price_tag.text  # 상품 가격

            # print(link, "+", prdName, "+", prdImg, "+", prdPrice)
            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('텐바이텐 남자친구 크롤링 저장 완료!')


# 1-7. 텐바이텐 부모님 크롤링
def txtMFUrl():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'http://www.10x10.co.kr/search/search_result.asp?rect=%EB%B6%80%EB%AA%A8%EB%8B%98+%EC%84%A0%EB%AC%BC&prvtxt=%EC%8A%A4%EC%8A%B9%EC%9D%98%EB%82%A0+%EC%84%A0%EB%AC%BC&rstxt=%EC%8A%A4%EC%8A%B9%EC%9D%98%EB%82%A0+%EC%84%A0%EB%AC%BC&extxt=&sflag=&dispCate=&cpg=1&chkr=False&chke=False&mkr=&sscp=N&psz=60&srm=be&iccd=&styleCd=&attribCd=&icoSize=M&arrCate=&deliType=&minPrc=&maxPrc=&lstDiv=search&subshopcd=&giftdiv=&prectcnt=1243',
        headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    items = soup.select('div.pdtWrap>ul>li ')
    genCode = 80;

    for item in items:
        a_tag = item.select_one('div>a')
        price_tag = item.select_one('div>div>p>span')

        if a_tag is not None:
            genCode
            link = "http://www.10x10.co.kr" + item.select_one('a')['href']  # 상품 링크
            prdName = item.select_one('img')['alt']  # 상품 이름
            prdImg = item.select_one('img')['src']  # 상품 이미지
            prdPrice = price_tag.text  # 상품 가격
            # print(link, "+", prdName, "+", prdImg, "+", prdPrice)
            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('텐바이텐 부모님 크롤링 저장 완료!')

def gen10Naver():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=10%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    test = soup.select('div.group_guide >ul >li')
    # img alt:상품이름 , img src:이미지링크 , em title,em.text:가격
    genCode = 10

    for test2 in test:
        a_tag = test2.select_one('div>a')

        # print(name)
        if a_tag is not None:
            link = test2.select_one('a')['href']  # 상품 링크
            prdName = test2.select_one('img')['alt']  # 상품 이름
            prdImg = test2.select_one('img')['src']  # 상품 이미지
            prdPrice = test2.select_one('em')['title']  # 상품 가격

            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('gen10Naver 크롤링 저장 완료!')

def gen20Naver():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=20%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    test = soup.select('div.group_guide >ul >li')
    genCode = 20
    # print(test)

    # img alt:상품이름, img src:상품 이미지, img src:이미지링크

    for test2 in test:
        a_tag = test2.select_one('div>a')
        name = test2.select_one('a')['href']
        # print(name)
        if a_tag is not None:
            link = test2.select_one('a')['href']  # 상품 링크
            prdName = test2.select_one('img')['alt']  # 상품 이름
            prdImg = test2.select_one('img')['src']  # 상품 이미지
            prdPrice = test2.select_one('em')['title']  # 상품 가격

            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('gen20Naver 크롤링 저장 완료!')


def gen30Naver():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=30%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&oquery=23%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&tqi=UzBh3sp0JXossbv15RGssssstR0-289751',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    test = soup.select('div.group_guide >ul >li')
    # img alt:상품이름 , img src:이미지링크 , em title,em.text:가격
    genCode = 30

    for test2 in test:
        a_tag = test2.select_one('div>a')

        # print(name)
        if a_tag is not None:
            link = test2.select_one('a')['href']  # 상품 링크
            prdName = test2.select_one('img')['alt']  # 상품 이름
            prdImg = test2.select_one('img')['src']  # 상품 이미지
            prdPrice = test2.select_one('em')['title']  # 상품 가격

            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('gen30Naver 크롤링 저장 완료!')


def gen40Naver():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=40%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&oquery=30%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&tqi=UzBh3wp0Jy0sshwe55NsssssshG-196664',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    test = soup.select('div.group_guide >ul >li')

    genCode = 40

    for test2 in test:
        a_tag = test2.select_one('div>a')

        # print(name)
        if a_tag is not None:
            link = test2.select_one('a')['href']  # 상품 링크
            prdName = test2.select_one('img')['alt']  # 상품 이름
            prdImg = test2.select_one('img')['src']  # 상품 이미지
            prdPrice = test2.select_one('em')['title']  # 상품 가격

            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('gen40Naver 크롤링 저장 완료!')

def gen50Naver():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=50%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&oquery=40%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&tqi=UzBh9lp0JXVssNU9YHKsssssti4-036491',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    # test = soup.select_one('#main_pack > div.sp_shop_default.section._shopping_guide_view > div.group_item > div.group_guide > div:nth-child(1) > div > ul > li:nth-child(1) > div > div.detail_area > div > div.tit > a')
    # test2 = soup.select('#main_pack > div.sp_shop_default.section._shopping_guide_view > div.group_item > div.group_guide > div:nth-child(1) > div > ul >li> div > div')
    test = soup.select('div.group_guide >ul >li')
    # img alt:상품이름 , img src:이미지링크 , em title,em.text:가격
    genCode = 50

    for test2 in test:
        a_tag = test2.select_one('div>a')

        # print(name)
        if a_tag is not None:
            link = test2.select_one('a')['href']  # 상품 링크
            prdName = test2.select_one('img')['alt']  # 상품 이름
            prdImg = test2.select_one('img')['src']  # 상품 이미지
            prdPrice = test2.select_one('em')['title']  # 상품 가격

            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('gen50Naver 크롤링 저장 완료!')

def gen10txt():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'http://www.10x10.co.kr/search/search_result.asp?rect=10%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&exkw=1',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    # print(soup)
    test = soup.select('div.pdtWrap>ul>li ')
    # print(test)
    genCode = 10

    # img alt=상품이름/img src=이미지/span class="finalP" = 가격
    for test2 in test:
        a_tag = test2.select_one('div>a')
        price_tag = test2.select_one('div>div>p>span')

        if a_tag is not None:
            link = test2.select_one('a')['href']  # 상품 링크
            prdName = test2.select_one('img')['alt']  # 상품 이름
            prdImg = test2.select_one('img')['src']  # 상품 이미지
            prdPrice = price_tag.text  # 상품 가격
            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('gen10txt 크롤링 저장 완료!')

def gen20txt():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'http://www.10x10.co.kr/search/search_result.asp?rect=20%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&exkw=1',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    # print(soup)
    test = soup.select('div.pdtWrap>ul>li ')
    # print(test)
    genCode = 20

    # img alt=상품이름/img src=이미지/span class="finalP" = 가격
    for test2 in test:
        a_tag = test2.select_one('div>a')
        price_tag = test2.select_one('div>div>p>span')

        if a_tag is not None:
            link = test2.select_one('a')['href']  # 상품 링크
            prdName = test2.select_one('img')['alt']  # 상품 이름
            prdImg = test2.select_one('img')['src']  # 상품 이미지
            prdPrice = price_tag.text  # 상품 가격
            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('gen20txt 크롤링 저장 완료!')

def gen30txt():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'http://www.10x10.co.kr/search/search_result.asp?rect=30%EB%8C%80+%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC&exkw=1',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    # print(soup)
    test = soup.select('div.pdtWrap>ul>li ')
    # print(test)

    genCode = 30

    # img alt=상품이름/img src=이미지/span class="finalP" = 가격
    for test2 in test:
        a_tag = test2.select_one('div>a')
        price_tag = test2.select_one('div>div>p>span')

        if a_tag is not None:
            link = test2.select_one('a')['href']  # 상품 링크
            prdName = test2.select_one('img')['alt']  # 상품 이름
            prdImg = test2.select_one('img')['src']  # 상품 이미지
            prdPrice = price_tag.text  # 상품 가격
            prdList = {
                'genCode': genCode,
                'prdLink': link,
                'prdImg': prdImg,
                'prdName': prdName,
                'prdPrice': prdPrice
            }
            db.HapB.insert_one(prdList)
    print('gen30txt 크롤링 저장 완료!')



# db 실행
# check = list(db.HapB.find({'genCode':60}))
# print(check)

# 네이버 여자친구 크롤링 저장 완료
# naverGfUrl()
# # 네이버 남자친구 크롤링 저장 완료
# naverBfUrl()
# # 텐바이텐 여자친구 크롤링 저장 완료
# txtGfUrl()
# # 텐바이텐 남자친구 크롤링 저장 완료
# txtBfUrl()
# # 텐바이텐 부모님 크롤링 저장 완료
# txtMFUrl()
# gen10Naver()
# gen20Naver()
# gen30Naver()
# gen40Naver()
# gen50Naver()
gen10txt()
gen20txt()
gen30txt()
