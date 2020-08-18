import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.10x10.co.kr/search/search_result.asp?rect=%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC+%EC%84%A0%EB%AC%BC&prvtxt=%EC%97%84%EB%A7%88+%EC%84%A0%EB%AC%BC&rstxt=%EC%97%84%EB%A7%88+%EC%84%A0%EB%AC%BC&extxt=&sflag=&dispCate=&cpg=1&chkr=False&chke=False&mkr=&sscp=N&psz=60&srm=be&iccd=&styleCd=&attribCd=&icoSize=M&arrCate=&deliType=&minPrc=&maxPrc=&lstDiv=search&subshopcd=&giftdiv=&prectcnt=869', headers=headers)

soup = BeautifulSoup(data.text,'html.parser')
# print(soup)
test = soup.select('div.pdtWrap>ul>li ')
# print(test)

# img alt=상품이름/img src=이미지/span class="finalP" = 가격
for test2 in test:
    a_tag = test2.select_one('div>a')
    price_tag = test2.select_one('div>div>p>span')

    if a_tag is not None:
        link = test2.select_one('a')['href'] #상품 링크
        prdName = test2.select_one('img')['alt'] #상품 이름
        prdImg = test2.select_one('img')['src'] #상품 이미지
        prdPrice = price_tag.text #상품 가격

        print(link,"+",prdName,"+",prdImg,"+",prdPrice)
