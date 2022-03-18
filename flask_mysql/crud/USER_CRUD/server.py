# Runthe below in your terminal to get started with you FLASK project
# pipenv install pymysql flask pipenv shell pip install cryptography
# then open your server python3 server.py
from pprint import pprint
from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from user import User
app = Flask(__name__)


@app.route('/')
@app.route('/users')
def users():
    # creates a list of class objects and then use the DOT notation to extract the information about them
    users = User.get_all()
    return render_template('users.html', users=users)


@app.route('/users/new')
def new():
    users = User.get_all()
    return render_template('create.html', users=users)


@app.route('/users/create', methods=['POST'])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # print(request.form)
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route('/users/<int:id>')
def show(id):
    data = {
        'id': id
    }
    user = User.view(data)
    return render_template('read(one).html', user=user)


@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edit.html', user=User.view(data))


@app.route('/users/<int:id>/destroy')
def destroy(id):
    data = {
        'id': id
    }
    User.destroy(data)
    return redirect('/users')


@app.route('/users/update', methods=['POST'])
def update():
    data = {
        "id": request.form['id'],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(data)
    a = request.form['id']
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
