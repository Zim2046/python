from pprint import pprint
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.user import Magazine

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")
## TODO handle registration with bcrypt
@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    pprint(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    print(user_id)
    session['user_id'] = user_id
    session['user_name'] = request.form['first_name'] + ' ' + request.form['last_name']
    return redirect("/dashboard")


## TODO handle login 
@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['user_name'] = user_in_db.first_name
    return redirect("/dashboard")

#TODO GETS all magazine data of a specific person, save it to 'user' and feeds it to html
@app.route('/show/<int:id>')
def show_user(id):
    data = {'id': id}
    magazine = Magazine.get_one(data)
    user = User.get_user_with_magazines(data)
    return render_template("show_magazine.html", user = user, magazine = magazine)

#TODO  DELETES all the session data on the way out
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')





