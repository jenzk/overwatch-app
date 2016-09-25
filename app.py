import os
from flask import Flask
from flask import jsonify, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/rankings')
def rankings():
    return render_template("rankings.html")

@app.route('/stats/<name>')
def stats(name):
    r = requests.get("http://ow-api.herokuapp.com/stats/pc/us/%s" % name)
    print r.text
    return render_template("stats.html", data=r.json())


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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
