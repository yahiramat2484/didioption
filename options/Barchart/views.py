from flask import jsonify, render_template
from options.app import app
from .trims import barchar
from .processing import get_top_pages
from .Models import Barchart
from options.admin.emails import send_options_data
import requests

@app.route("/")
def home():
    render_template("home.html")

@app.route("/sendemail")
def send_email():
    options = requests.get(barchar)
    new_row = Barchart()
    new_row.data = options.json()
    send_options_data(options.json())
    new_row.save()
    get_top_pages()
    return jsonify({"status": "ok"})