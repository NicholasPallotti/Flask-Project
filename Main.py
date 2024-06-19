from flask import Flask, url_for, request, render_template, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.mydatabase
decks = db.decks

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        deck_name = request.form['deck_name']
        format = request.form['format']
        decks.insert_one({'name':deck_name, 'format': format})
        return redirect(url_for('index'))

    all_decks = decks.find()
    return render_template('index.html', decks=all_decks)

@app.post("/<id>/delete/")
def delete(id):
    decks.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
