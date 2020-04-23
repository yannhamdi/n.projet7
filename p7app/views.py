from flask import Flask, render_template, jsonify, request

from . import parsing as par

from . import googlemapapi as goo

from . import pybot as py 


app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.

# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
@app.route('/p7homepage/')
def index():
    return render_template("p7homepage.html")


@app.route('/sendingServer', methods=["POST"])
def sending_question():
    user_question = request.form["question"]
    client_treatment = py.PapyBot()
    client_treatment.transformed_gps_into_json_results(user_question)
    return jsonify([client_treatment.sending_gps_coordinate])


if __name__ == "__main__":
    app.run()