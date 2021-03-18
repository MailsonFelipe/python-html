from app import app
import flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")