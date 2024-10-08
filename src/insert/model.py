import os
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': os.getenv("MONGO_URI"),
    'tls': 'true',
    'ssl_cert_reqs': 'CERT_NONE'
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    login    = db.StringField(unique=True,required=True)
    name     = db.StringField(max_length=80,required=True)
    email    = db.EmailField(max_length=80,required=True)
    comments = db.ListField(db.DictField())
    def to_json(self):
        return {"login": self.login,
                "name": self.name,
                "email": self.email,
                "comments": self.comments}
