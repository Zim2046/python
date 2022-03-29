import re
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

## 👇 handling registration with bcrypt
@app.route('/register/user', methods=['POST'])
def register():
    # if there are errors:
    #👇 we call the staticmethod in Class(User) model to validate
    if not User.validate_user(request.form):
        # redirect to the route where the login & reg form is rendered.
        return redirect('/')
    #👇 create the password hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    #👇 put the pw_hash into the data dictionary
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    #👇 Call the save @classmethod on User
    user_id = User.save(data)
    #👇 Save the user id & name in the cookies
    session['user_id'] = user_id
    session['name'] = request.form['first_name']
    return redirect("/dashboard")

@app.route('/login', methods=['POST'])
def login():
    #👇 see if the email provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    #👇 if user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        #👇 if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    #👇 if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['name'] = user_in_db.first_name
    return redirect("/dashboard") #👈 never render on a post!!!

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

