from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods = ['POST'])

def index():
    if request.method=='POST':
        return '<h1> Deployed to heroku!!!</h1>'
