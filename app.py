from flask import Flask
app = Flask(__name__)

@app.route('/entry', methods = ['POST'])

def index():
    return '<h1> Deployed to heroku!!!</h1>'
