from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("checkerboard.html")


@app.route('/other/<string:name>/<int:num>')
def other(name, num):
    return render_template("newStuff.html", user=name, digit=num, phrase='Im just a dude, disguised as another dude!')


@app.route('/success')
def success():
    return "Success"


# @app.route('/index/<string:username>/<int:id>')
# def index(username, id):
#     return render_template("index.html", username=username, id=id)


# app.run(debug=True) should be the very last statement!
if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
