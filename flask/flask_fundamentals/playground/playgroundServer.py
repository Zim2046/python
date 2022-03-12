# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


@app.route('/play')
def play():
    return render_template('playgroundServer.html', phrase="Welcome!", num=3, color='lightblue',     padding='345'
                           )


@app.route('/play/<int:num>')
def play2(num):
    return render_template('playgroundServer.html', phrase="Welcome!", num=num, color='lightblue', padding='23')


@app.route('/play/<int:num>/<string:color>')
def play3(num, color):
    return render_template('playgroundServer.html', phrase="Welcome!", num=num, color=color, padding='23')


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
# comments
