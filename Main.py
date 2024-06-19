from flask import Flask, url_for, request, render_template, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.newdatabase
decks = db.decks

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        format = request.form['format']
        decks.insert_one({'name':name, 'format': format})
        return redirect(url_for('index'))

    all_decks = decks.find()
    
    #for x in all_decks:
        #print(x)
    print()
    print()
    return render_template('index.html', decks=all_decks)

@app.post("/<id>/delete/")
def delete(id):
    decks.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
