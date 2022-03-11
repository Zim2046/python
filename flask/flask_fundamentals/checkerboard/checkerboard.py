from turtle import color
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def square():
    return render_template("checkerboard.html", colDimension=8, rowDimension=8, colorOne='red', colorTwo='black')


@app.route('/<int:height>')
def rect(height):
    return render_template("checkerboard.html", colDimension=height, rowDimension=8,  colorOne='red', colorTwo='black')


@app.route('/<int:width>/<int:height>')
def custom(width, height):
    return render_template("checkerboard.html", colDimension=height, rowDimension=width,  colorOne='red', colorTwo='black')


@app.route('/<int:width>/<int:height>/<string:colorOneIn>/<string:colorTwoIn>')
def customColor(width, height, colorOneIn, colorTwoIn):
    return render_template("checkerboard.html", colDimension=height, rowDimension=width,  colorOne=colorOneIn, colorTwo=colorTwoIn)


# app.run(debug=True) should be the very last statement!
if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
