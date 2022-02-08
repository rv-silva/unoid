from flask import Flask, request
app = Flask(__name__)

@app.route('/entry/unoid', methods=['GET', 'POST'])
def unoid():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of users',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
		'body': request.json
        }

@app.route('/entry/unoid/<int:uno_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(uno_id):
    if request.method == "GET":
        return {
            'id': uno_id,
            'message': 'This endpoint should return the entity {} details'.format(uno_id),
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
