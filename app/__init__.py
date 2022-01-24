import pymongo

from flask import Flask

from app import routes as posts_view

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["kenzie"]

def create_app():

    app = Flask(__name__, static_folder=None)
    app.config["JSON_SORT_KEYS"] = False
    posts_view.init_app(app)

    return app
