from flask import Flask, render_template, jsonify, request


from . import parsing as par 


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
    client_treatment = par.SentenceParse()
    client_treatment.in_lower_case(user_question)
    print(client_treatment.sentence)
    return jsonify(["pas de reponse"])


if __name__ == "__main__":
    app.run()