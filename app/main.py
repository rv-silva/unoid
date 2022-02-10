import pymongo, os
from flask import Flask, request

app = Flask(__name__)

# Set connection to MongoDB, Database & Collection
conn_str = os.getenv("DB_ADDRESS")
cluster = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = cluster["users"]
collection = db["userdata"]

@app.route("/unoid/<string:uid>", methods=["GET"])
def get_unoid(uid):
    results = collection.find({"_id": uid})
    return {
        'id': uid,
        'message': 'UnoID {} details'.format(results),
        'method': request.method
    }

@app.route("/unoid/", methods=["POST"])
def new_unoid():
    collection.insert_one(request.json)
    return {
        'message': 'UnoID created successfully',
        'method': request.method,
    'body': request.json
    }
