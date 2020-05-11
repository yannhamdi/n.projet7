from flask import Flask, render_template, request, jsonify

from . import parsing as par

from . import googlemapapi as goo

from . import pybot as py 

import os


app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
@app.route('/p7homepage/')
def index():
    return render_template("p7homepage.html",api_key = os.getenv("KEY_API"))


@app.route('/sendingServer', methods=["POST"])
def sending_question():
    user_question = request.form["question"]
    client_treatment = py.PapyBot()
    client_treatment.transformed_gps_into_json_results(user_question)
    client_treatment.transformed_pageid_into_json(client_treatment.gps_lat, client_treatment.gps_lng)
    client_treatment.transformed_info_js(client_treatment.pageid_for_js)
    client_treatment.returning_dictionnary(client_treatment.info, client_treatment.url, client_treatment.gps_adress, client_treatment.lat, client_treatment.lng)
    response = client_treatment.data_treated
    return jsonify(response)


if __name__ == "__main__":
    app.run()