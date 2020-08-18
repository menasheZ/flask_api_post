import flask
import requests
from flask import request

import men_json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    url = 'http://127.0.0.1:5000/second-post'
    my_obj = {"first_name": "menashe", "last_name": " zinger", "the_answer": "#42"}
    x = requests.post(url, json=my_obj)
    return "<h1>" + x.text + "</h1>"


@app.route('/second-post', methods=['POST'])
def try_view3():
    this_json = request.get_json()
    s1: str = men_json.return_string(this_json)
    return s1


@app.route("/", methods=['POST'])
def this_post():
    response = requests.post('/', json={'id': 1, 'name': 'x'})
    return "OK"


app.run()
