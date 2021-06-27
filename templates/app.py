from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

#client = MongoClient('mongodb+srv://riken:<riken>@cluster0.svy8k.mongodb.net/line?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE&authSource=admin')

client = MongoClient('mongodb://localhost:27017') #Local DB for testing purposes, will need to replace with Cloud connection later

db = client['line']
collection = db['charts']

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# app.config['MONGO_DBNAME'] = 'line'
# app.config['MONGO_URI'] = 'mongodb+srv://riken:<riken>@cluster0.svy8k.mongodb.net/line?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE&authSource=admin'


mongo = PyMongo(app)

@app.route('/')
@cross_origin()
def index():
    return render_template('chart.html')

@app.route('/data')
def data():

    #Search String provided by User from Dropdown Menu
    id = request.args.get('name')
    print("Name: " + id)

    # Find collection with matching name as Search String in DB
    result = collection.find_one({'name': id})


    #charts = client.line
    #print(result['predicted'])
    #print(result['actual'])

    # Return correct data
    return jsonify({'results':{'predicted': result['predicted'], 'actual': result['actual'], 'xlabel': result['xlabel'], 'xvalues':result['xvalues']}})



if __name__ == '__main__':
    app.run(debug=True)