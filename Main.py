from flask import Flask, request, render_template
from flask_pymongo import PyMongo
#import pymongo

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient['testdatabase']
#mycol = mydb["test"]

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
        online_users=online_users)
#
#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"
#

@app.get('/login')
def login_get():
     return 'get login'

@app.post('/login')
def login_post():
     return 'post login'

@app.route('/decks/')
def decks():
      return
