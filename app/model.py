import os
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': os.getenv("MONGO_URI")
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}
