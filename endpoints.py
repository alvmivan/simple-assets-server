from markupsafe import escape
from flask import Flask, request
import repo

app = Flask(__name__)


@app.route("/fetch_data/<data_type>/<name>", methods=["GET"])
def get_data(data_type, name):
    code = escape(name)
    return repo.retrieve_data(code, data_type)


@app.route("/save_data/<data_type>/<name>", methods=["POST"])
def save_data(data_type, name):
    data = request.data
    repo.save_data(escape(name), data, escape(data_type))
    return "200"


@app.route("/get_codes/<data_type>", methods=["GET"])
def get_codes(data_type):
    return repo.get_codes_for_type(escape(data_type))


