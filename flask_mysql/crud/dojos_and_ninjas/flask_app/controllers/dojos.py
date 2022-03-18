from flask import render_template, request, session, flash, redirect
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', dojos=dojos)


@app.route('/')
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', dojos=dojos)
