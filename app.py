from flask import Flask, jsonify,request,json
from scrapper import scrap_cards
from config import *
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/scrap', methods = ['POST'])
def generate_json():
    req = request.get_json(force=True)
    print(req['url'])
    scrap_cards(req['url'])
    data = json.load(open(JSON_FOLDER+'output.json'))
    return jsonify(data)

if __name__ == '__main__':
    app.run()
