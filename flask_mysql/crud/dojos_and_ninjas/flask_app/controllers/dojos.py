from pprint import pprint
from flask_app import app
from flask import render_template,redirect,request,session, flash

from flask_app.models.dojo import Dojo
@app.route('/')
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

@app.route("/create/dojo", methods=["POST"])
def create_dojo():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not Dojo.validate_dojo(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    Dojo.save(request.form)
    print(request.form)
    Dojo.save(request.form)
    return redirect('/')

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = { 'id': id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("show_dojo.html", dojo = dojo)
