from flask import render_template, request, session, redirect
from flask_app import app
from flask_app.models.ninja import Ninja


@app.route('/')
@app.route('/ninja')
def dojos():
    ninja = Ninja.get_all()
    print(ninja)
    return render_template('dojos.html', dojos=ninja)


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', dojos=dojos)
