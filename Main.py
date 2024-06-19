from flask import Flask, url_for, request, render_template, redirect
from pymongo import MongoCLient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.mydatabase
decks = db.decks

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POSt':
        content = request.form['content']

    all_decks = decks.find()
    return render_template('index.html', decks=all_decks)

if __name__ == "__main__":
    app.run(debug=True)
