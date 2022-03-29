from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.magazine import Magazine

#TODO CREATE
#TODO Show the new magazine form
@app.route('/new')
def new_magazine():
    return render_template('new_magazine.html')

## TODO handle new magazine form
@app.route('/create/new', methods=['POST'])
def create_magazine():
    print(request.form)
    data = {'title': request.form['title'],
            'description': request.form['description'],
            'user_id': int(request.form['user_id'])}
    Magazine.save(data) #todo class method in magazine class, find it in ../controllers/magazine.py
    return redirect('/dashboard')

#TODO READ
@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect('/logout')
    
    users_and_mags = Magazine.get_all_both()
    return render_template('dashboard.html', users_and_mags = users_and_mags)




#TODO UPDATE
# TODO route to edit magazine form
@app.route('/magazines/<int:id>/edit')
def edit_magazine(id):
    data = {'id': id}
    magazine = Magazine.get_one(data)
    return render_template('edit_magazine.html', magazine = magazine)

# TODO handle magazine edit
@app.route('/edit/magazine', methods=['POST'])
def update_magazine():
    print(request.form)
    magazine = Magazine.update(request.form)
    print(magazine)
    return redirect(f"/magazines/{request.form['id']}")

#TODO DELETE
@app.route('/delete/<int:id>')
def destroy_magazine(id):
    data = {'id':id}
    Magazine.destroy(data)   #TODO class method in User class, find it in ../controllers/user.py
    return redirect('/magazines')
