from flask import Flask, request, render_template, flash, redirect, url_for
from datetime import datetime
from dotenv import load_dotenv
import os
import requests
load_dotenv()
BACKEND_URL = os.getenv('BACKEND_URL')
app = Flask(__name__)
app.secret_key = "secret123"
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)