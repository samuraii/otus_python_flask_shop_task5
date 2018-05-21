from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/description')
def description():
    return render_template('description.html')


@app.route('/prices')
def prices():
    return render_template('prices.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/analogs')
def analogs():
    return render_template('analogs.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
