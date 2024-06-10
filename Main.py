from flask import Flask
from markupsafe import escape
import pymongo

app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["Decks"]

mylist = [
      {"name": "amulet yitan", "format": "modern"},
      {"name": "8-cast", "format": "legacy"},
      {"name": "death and taxes", "format": "legacy"},
]

x = mycol.insert_many(mylist)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
        return f"Hello, {escape(name)}!"

@app.route('/projects/')
def projects():
      return 'The project page'

@app.route('/decks/')
def decks():
      return "this will eventually be a list of decks"
