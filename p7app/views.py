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
    return render_template("p7homepage.html",api_key = app.config['KEY_API'])


@app.route('/sendingServer', methods=["POST"])
def sending_question():
    user_question = request.form["question"]
    client_treatment = py.PapyBot()
    client_treatment.transformed_gps_into_json_results(user_question)
    response = client_treatment.sending_gps_coordinate
    print(response)
    return jsonify(response)


if __name__ == "__main__":
    app.run()