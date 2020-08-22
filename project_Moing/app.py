from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbmoing

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


@app.route('/recommend')
def recommend():
    return render_template('introducePrd.html')

#연령별 상품 추천 페이지 보여주기
@app.route('/recommend', methods=['GET'])




if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)