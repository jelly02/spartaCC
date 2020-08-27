from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.moing

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# 로그인 화면 보여주기
@app.route('/login')
def logintoss():
    return render_template('login.html')

# 회원가입 화면 보여주기
@app.route('/sign')
def signup():
    return render_template('sign-up.html')

#연령별 상품 추천 페이지 보여주기
@app.route('/recommend')
def recommend():
    return render_template('introducePrd.html')

#유저들이 뽑은 생일선물 투표 페이지 보여주기
@app.route('/userChoose')
def userChoose():
    return render_template('userChoose.html')

@app.route('/userChooseGet',methods=['POST'])
def userChooseGet():
    choose = request.form['user_give']
    print(choose)
    # plus = db.vote.fine_one({})


@app.route('/recommend2',methods=['GET'])
def test():

    # 1. 유저가 선택한 연령대 숫자를 받고
    gen_receive = request.args.get('genNum')

    # Check type of gen_receive
    # print(type(gen_receive))

    # if ger_recevie == int -> str(gen_receive)
    # if gen_receive == str -> int(gen_receive)

    # 2. DB에 해당 연령대 상품들을 가져와서 / id:False를 안 하면 직렬화 에러가 난다
    result = list(db.HapB.find({'genCode':int(gen_receive)}, {'_id': False}))
    # print("여긴 back이야",result)

    # 3. prdList에 담아 보낸다
    return jsonify({'result': 'success', 'prdList': result})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)