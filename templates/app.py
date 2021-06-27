from flask import Flask, render_template, jsonify
from random import sample
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['MONGO_DBNAME'] = 'line'
app.config['MONGO_URI'] = 'mongodb+srv://riken:<riken>@cluster0.svy8k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
#
mongo = PyMongo(app)

@app.route('/')
@cross_origin()
def index():
    return render_template('chart.html')

@app.route('/data')
def data():
    charts = mongo.db.line
    #
    result = charts.find_one({'name':'Chart1'})
    return jsonify({'results': result['values']})


@app.route('/labels')
def labels():
    # charts = mongo.db.line
    #
    # result = charts.find_one({'name':'Chart1'})

    return jsonify({'results': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']})


if __name__ == '__main__':
    app.run(debug=True)