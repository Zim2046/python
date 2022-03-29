from pprint import pprint
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def make_ninja(): 
    return render_template("ninjas.html", dojos = Dojo.get_all())

@app.route('/create/ninja', methods=["POST"])
def create_ninja():
    # print("In route", request.form)
    Ninja.save(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")


