import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.artboxmall.com/home/shop/category.asp?cdl=500&cdm=256&page=1&ord=o5', headers=headers)

soup = BeautifulSoup(data.text,'html.parser')
test = soup.select('body > div.wrap > section.sec_cont > form > div > ul')
test0 = test.select_one('li>a')

print(test0)



# for test2 in test:
#     a_tag = test2.select_one('li >a')
#     print(a_tag)
#    price_tag=test2.select_one('span.price') 출력 안됨

    # if a_tag is not None:
    #     link = test2.select_one('a')['href']  # 상품 링크
    #     prdName = test2.select_one('a')['title']  # 상품 이름
    #     prdImg = test2.select_one('img')['src']  # 상품 이미지
    #     # prdPrice = price_tag.text  # 상품 가격
    #
    #     print(prdName)
