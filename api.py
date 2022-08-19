from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'Sangeetha',
        'items': [
            {
                'name': 'MI note 10',
                'price': 10000
            }
        ]
    },
    {
        'name': 'Sangeetha 2',
        'items': [
            {
                'name': 'MI note 11',
                'price': 100
            }
        ]
    }
]


@app.route('/')
def home():
    return "Welcome to Api"


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_all_store_name():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


app.run(port=5000)