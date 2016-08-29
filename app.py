from flask import Flask
from flask import jsonify, render_template
import requests


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello-json')
def hello_json():
    return jsonify(hello="world")

@app.route('/overwatch-data')
def overwatch_data():
    r = requests.get("https://api.lootbox.eu/patch_notes")
    print r.text
    return jsonify(data=r.json())

@app.route('/overwatch-table')
def overwatch_table():
    r = requests.get("https://api.lootbox.eu/patch_notes")
    return render_template("overwatch_table.html", data=r.json())
