from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',page='index')

@app.route('/mision')
def about():
    return render_template('mision.html',page='mision')