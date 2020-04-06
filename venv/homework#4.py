from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework#4.html')


@app.route('/orders', methods=['POST'])
def make_order():
    lastname_receive = request.form['lastname_give']
    firstname_receive = request.form['firstname_give']
    age_receive = request.form['age_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    contact_receive = request.form['contact_give']

    order = {
        'lastname': lastname_receive,
        'firstname': firstname_receive,
        'age': age_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'contact': contact_receive,
    }
    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 작성되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)
