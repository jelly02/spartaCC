from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbmoing
#연령별 상품 추천 페이지 보여주기
@app.route('/recommend', methods=['POST'])
def recommend():
    return render_template('introducePrd.html')

    #유저가 선택한 연령대 숫자를 받고
    # user_num = request.form['genNum']
    # print(user_num)
    # #DB에 해당 연령대 상품들을 가져와서
    # result = list(db.genList.find({'genNum' : user_num}))
    # #prdList에 담아 보낸다
    # return jsonify({'result':'success', 'prdList':result})

@app.route('/recommend2', methods=['POST'])
def recommend_toss():

    # 유저가 선택한 연령대 숫자를 받고
    user_num = request.args.get('genNum')
    print(user_num)
    #DB에 해당 연령대 상품들을 가져와서
    result = list(db.genList.find({'genNum' : user_num}))
    #prdList에 담아 보낸다
