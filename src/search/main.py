#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify

from model import User

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    login = request.args.get('login')
    user = User.objects(login=login).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True)
