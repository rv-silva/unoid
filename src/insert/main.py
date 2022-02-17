#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify

from model import User

app = Flask(__name__)

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    user = User(login=record['login'],
                name=record['name'],
                email=record['email'])
    user.save()
    return jsonify(user.to_json())

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    user = User.objects(login=record['login']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(name=record['name'],
                    email=record['email'],
                    add_to_set__comments=record['comments'])
        user = User.objects(login=record['login']).first()
    return jsonify(user.to_json())

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(login=record['login']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True)
