from flask import  Flask, render_template,jsonify,request
#render_template : flask와 html 연결

app = Flask(__name__)

#--------- url 방식 짜기---------

# default 경로 / 여기로 들어오면 아래 html 문서 띄워줌
@app.route('/')
def say_hello():
    return render_template('index.html')

# 이 경로를 get(받을 때)으로 들어오면 해당 함수 실행 / 물론 POST(보낼 때) 방식도 가능
@app.route('/test',methods=['GET'])
def test():
    title = request.args.get('title_give') #title_give가 있니? 있으면 가져와줘
    print(title)
    #jsonify : 괄호 안에 있는 내용들을 json 방식으로 보여줌 / key 알파벳 순으로 정렬 / 사전 방식으로 출력
    return jsonify({'result': 'success', 'msg': 'GET method'})

# 유저 입장
@app.route('/test',methods=['POST'])
def test_post():
    receive_data = request.form['title'] #유저가 보낸 title 내용을 받는 변수
    print(receive_data)
    return jsonify({'result': 'success', 'msg': 'POST method'})

if __name__ == '__main__':
    app.run('127.0.0.1', port=8000, debug=True)
