from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost',27017)
db = client.week4db

@app.route('/')
def go_index():
    return render_template('index.html')

#리스트 읽어오기
@app.route('/order', methods=['GET'])
def read_list():

    db_list = list(db.order_db.find({},{'_id':0}))
    print(db_list)

    return jsonify({'result': 'success', 'db_list': db_list})

#order 보내기
@app.route('/order',methods=['POST'])
def send_order():
    db_name = request.form['name_send']
    db_piece = request.form['piece_send']
    db_add = request.form['add_send']
    db_num = request.form['num_send']

    order_db = {
        'name' : db_name,
        'piece': db_piece,
        'address': db_add,
        'number': db_num
    }

    db.order_db.insert_one(order_db)
    return jsonify({'result':'success','msg':'주문이 완료되었습니다:)'})

if __name__ == '__main__':
    app.run('127.0.0.1', port=5002, debug=True)
