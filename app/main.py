import pymongo, os
from flask import Flask, request

app = Flask(__name__)

# Set connection to MongoDB, Database & Collection
conn_str = os.getenv("DB_ADDRESS")
cluster = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = cluster["users"]
collection = db["userdata"]

@app.route('/entry/unoid', methods=['GET', 'POST'])
def unoid():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of users',
            'method': request.method
        }
    if request.method == "POST":
        collection.insert_one(request.json)
        return {
            'message': 'UnoID created successfully',
            'method': request.method,
		'body': request.json
        }

@app.route('/fetch/unoid/', methods=['GET', 'PUT', 'DELETE'])
def entity():
    uno_id = request.args.get('uno_id')
    if request.method == "GET":
        results = collection.find({"_id": uno_id})
        return {
            'id': uno_id,
            'message': 'UnoID {} details'.format(results),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': uno_id,
            'message': 'This endpoint should update the entity {}'.format(uno_id),
            'method': request.method,
		'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': uno_id,
            'message': 'This endpoint should delete the entity {}'.format(uno_id),
            'method': request.method
        }
