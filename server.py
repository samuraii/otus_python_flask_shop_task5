from flask import Flask
from flask import render_template
import json
app = Flask(__name__)

with open('data/data.json') as raw_data:
    data = json.load(raw_data)

@app.route('/')
def index():
    return render_template('index.html', data=data)


@app.route('/item/<id>')
def item(id):
    return render_template('item.html', id=id)


@app.route('/item/<id>/description')
def description(id):
    return render_template('description.html',id=id)


@app.route('/item/<id>/prices')
def prices(id):
    return render_template('prices.html', id=id)


@app.route('/item/<id>/feedback')
def feedback(id):
    return render_template('feedback.html', id=id)


@app.route('/item/<id>/analogs')
def analogs(id):
    return render_template('analogs.html', id=id)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
