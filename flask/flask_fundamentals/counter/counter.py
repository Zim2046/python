from itertools import count
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe!'
# our index route will handle rendering our form


@app.route('/')
def index():
    print(session)
    if 'count' in session:
        print('count exists!')
        session['count'] = session['count'] + 1
    else:
        print("key 'count' does NOT exist in session yet")
        session['count'] = 1
        print(session['count'])

    if 'actual_visits' in session:
        print('actual_visits exists!')
        session['actual_visits'] = session['actual_visits'] + 1
    else:
        print("key 'count' does NOT exist in session yet")
        session['actual_visits'] = 1
        print(session['actual_visits'])

    return render_template("counter.html")


@app.route('/count', methods=['POST'])
def count():
    print(session['count'])
    return redirect('/')
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.


@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    print(session)
    print(request.form)
    print(session['count'])
    session.pop('actual_visits')
    return redirect('/')
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.


@app.route('/add2', methods=['POST'])
def add2():
    print(session)
    print(session['count'])
    session['count'] = session['count'] + 2
    return render_template("counter.html")
# Never render a template on a POST request.
# Instead we will redirect to our index route.


@app.route('/incrementChoice', methods=['POST'])
def incrementChoice():
    session['count'] = (session['count'] + int(request.form['increment']))
    return render_template("counter.html")
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.


# app.run(debug=True) should be the very last statement!
if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)      # Run the app in debug mode.
