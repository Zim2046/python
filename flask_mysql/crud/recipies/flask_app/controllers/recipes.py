import re
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from datetime import datetime

#TODO ADD controller route 
@app.route('/recipes/add', methods=['POST'])
def add():
    # if there are errors:
    #👇 we call the staticmethod in Class(User) model to validate
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        # redirect to the route where the login & reg form is rendered.
        return redirect('/recipes/new')
    data = {
        "name": request.form['name'],
        "under_thirty": request.form['under_thirty'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "user_id": request.form['user_id'],
    }
    #👇 Call the save @classmethod on User
    Recipe.save(data)
    return redirect("/dashboard")

#TODO controller route validate user is logged in and route to the ADD HTML
# 👇 The following is used as controllers for 'Add New Recipe' actions
@app.route('/recipes/new')
def new():
    if 'user_id' not in session:
        return redirect('/logout')

    return render_template('new.html')

#TODO EDIT controller route 
@app.route('/recipes/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edit.html', recipe=Recipe.get_one_recipe(data))

#TODO UPDATE controller route 
@app.route('/recipes/update', methods=['POST'])
def update():
    data = {
        "id": request.form['id'],
        "name": request.form['name'],
        "under_thirty": request.form['under_thirty'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
    }
    Recipe.update(data)
    return redirect("/dashboard")

#TODO DELETE controller route 
@app.route('/recipes/destroy<int:id>/')
def destroy(id):
    data = {
        'id': id
    }
    Recipe.destroy(data)
    return redirect("/dashboard")

#TODO SHOW controller route 
@app.route('/recipes/show/<int:id>')
def show(id):
    data = {
        'id':id,
    }
    recipe = Recipe.show(data)
    print(type(recipe.made_on))
    date_object = datetime.strptime(recipe.made_on, "%Y-%m-%d %H:%M:%S") # Turn recipe.made_on into a 'date time object' first using 'strptime' and date format in 2022-03-27 00:24:08
    dateReFormatted = date_object.strftime("%B %d, %Y") # use the 'date time object' and reformat it how ever you want using 'strftime'
    print("Output of new date:", dateReFormatted)
    print("date_object =", date_object)
    print("type of date_object =", type(date_object))

    return render_template('show.html', recipe=recipe, dateReFormatted=dateReFormatted)

