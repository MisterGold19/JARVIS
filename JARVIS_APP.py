from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_in')
def sign_in_user():
    return render_template('sign_in.html')

@app.route('/sign_up')
def sign_up_user():
    return render_template('sign_up.html')
