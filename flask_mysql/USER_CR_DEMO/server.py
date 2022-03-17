# Runthe below in your terminal to get started with you FLASK project
# pipenv install pymysql flask pip install cryptography pipenv shell
# then open your server python3 server.py

from crypt import methods
from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    # creates a list of class objects and then use the DOT notation to extract the information about them
    users = User.get_all()
    return render_template('users.html', users=users)


@app.route('/user/new')
def new():
    return render_template('create.html')


@app.route('/user/create', methods=['POST'])
def create():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    print(request.form)
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
