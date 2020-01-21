from flask import Flask
app = Flask(__name__)

@app.route('/', methods = ['POST'])

def index():
    return '<h1> Deployed to heroku!!!</h1>'
