from itertools import count
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe!'
# our index route will handle rendering our form


@app.route("/")
def index():
    print(session)
    return render_template("dojo_survey.html")


@app.route("/result", methods=["POST"])
def result():
    print(request.form["name"])
    print(session)
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["gender"] = request.form["gender"]
    if request.form.get('online'):
        session["online"] = request.form["online"]
    else:
        session["online"] = 'No'
    if request.form.get('onsite'):
        session["onsite"] = request.form["onsite"]
    else:
        session["onsite"] = 'No'
    if request.form.get('noPreference'):
        session["noPreference"] = request.form["noPreference"]
    else:
        session["noPreference"] = 'No'
    session["comment"] = request.form["comment"]

    return render_template("result.html")


# app.run(debug=True) should be the very last statement!
if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)      # Run the app in debug mode.
