""" main.py: Entry file """
from flask import Flask, render_template, request, jsonify
import json
from waitress import serve

PRODUCTION_READY = 0
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/post-data", methods=['POST'])
def post_data():
    data = request.json
    if data:
        print(data)
        with open('db.json', 'w') as db:
            db.write(json.dumps(data))
        return jsonify({"res": "data posted success"})
    return jsonify({"err": "please provide data or read the doc for more info."}), 400

if PRODUCTION_READY:
    # for production
    serve(app, '0.0.0.0', threads=4)
app.run(debug=True, port=8000)