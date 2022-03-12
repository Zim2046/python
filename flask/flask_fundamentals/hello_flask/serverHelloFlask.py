from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    return render_template("indexHelloFlask.html", userName=name, times=num)


@app.route('/other/<string:name>/<int:num>')
def other(name, num):
    return render_template("indexHelloFlask.html", userName=name, times=num, phrase='Im just a dude, disguised as another dude!')


@app.route('/success')
def success():
    return "Success"


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("indexHelloFlask.html", random_numbers=[3, 1, 5], students=student_info)


# @app.route('/index/<string:username>/<int:id>')
# def index(username, id):
#     return render_template("index.html", username=username, id=id)


# app.run(debug=True) should be the very last statement!
if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
