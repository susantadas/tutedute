from flask import Flask, request, render_template, flash, redirect, url_for
from datetime import datetime
from dotenv import load_dotenv
import os
import requests
load_dotenv()
import os
import pymongo
DB_LINK = os.getenv('DB_LINK')
client = pymongo.MongoClient(DB_LINK)
db = client.susanta
userCollection = db['todo']
BACKEND_URL = os.getenv('BACKEND_URL')
app = Flask(__name__)
app.secret_key = "secret123"
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/')
def home():
    return render_template('todo.html')
@app.route('/api')
def api():
    with open('file.json') as f:
        data = json.load(f)
    return jsonify(data)
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.form
    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }
    collection.insert_one(item)
    return jsonify({"message": "Item saved successfully"})
if __name__ == "__main__":
    app.run(debug=True)