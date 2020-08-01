from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분 / 클라이언트가 서버로 POST로 보냄
@app.route('/review', methods=['POST'])
def write_review():
    # 1. 클라이언트가 보내준 정보 title, author, review 가져오기.
    title = request.form['title_send'] #클라이언트는 무조건 id 값으로 보내야함 ['key']
    author = request.form['author_send']
    review = request.form['review_send']

    # print("parsing 성공")
	
    # 2. DB에 정보 삽입하기 / key-value의 방식
    review_db = {
        'title': title,
        'author': author,
        'review': review
    }
    # db 저장
    db.review_db.insert_one(review_db)
    
    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '리뷰가 등록되었습니다'})


@app.route('/review', methods=['GET'])
def read_reviews():
    #db에 있는 모든 review 정보 가져오기 /▼ 파이썬 문법 (id를 제외한 전부)
    reviews = list(db.review_db.find({},{'_id':0}))

    return jsonify({'result': 'success', 'reviews': reviews})
#    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)