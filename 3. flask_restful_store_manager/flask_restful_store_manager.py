from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class Item(Resource):
    def get(self,name):
        return "post"
    def post(self,name):
        return "post"

api.add_resource(Item,"/item/<string:name>")
app.run(port=5000,debug=True)
