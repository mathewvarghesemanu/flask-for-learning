from flask import Flask, jsonify, request
app=Flask(__name__)

stores=[
    {
        'name':'suryastores',
        'items':
        [
            {
                'name':'pen',
                'price':10
            }
        ]
    }
]
@app.route('/')
def home():
    return "store manager app"

@app.route('/store',methods=['POST'])
def create_store():
    request_body=request.get_json()
    new_store={
                'name':request_body['name'],
               'items':[]
               }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>',methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name']==name:
            return(jsonify(store))
    return(jsonify({'ErrorMessage':'store not found'}))


@app.route('/store',methods=["GET"])
def get_stores():
        return jsonify({'stores':stores})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_body=request.get_json()
    new_item={'name':request_body['name'],'price':request_body['price']}
    for store in stores:
        if store['name']==name:
            store['items'].append(new_item)
            return (jsonify(new_item))
    return(jsonify({'errormessage':'store not found'}))

@app.route('/store/<string:name>/item',methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return (jsonify({'items':store['items']}))
    return (jsonify({'ErrorMessage': 'item not found'}))


app.run(debug=True,port=8000)