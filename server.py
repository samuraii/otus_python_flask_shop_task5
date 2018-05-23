from flask import Flask
from flask import render_template
import json
import io
app = Flask(__name__)

data = json.load(io.open('data/data.json', 'r', encoding='utf-8-sig'))

@app.route('/')
def index():
    return render_template('index.html', data=data)


@app.route('/item/<id>/')
def item(id):
    return render_template('item_main.html', id=id, data=data)


@app.route('/item/<id>/description')
def description(id):
    return render_template('description.html',id=id, data=data)


@app.route('/item/<id>/prices')
def prices(id):
    return render_template('prices.html', id=id, data=data)


@app.route('/item/<id>/feedback')
def feedback(id):
    return render_template('feedback.html', id=id, data=data)


@app.route('/item/<id>/analogs')
def analogs(id):
    return render_template('analogs.html', id=id, data=data)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
