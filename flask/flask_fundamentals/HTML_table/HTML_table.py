from flask import Flask, render_template
app = Flask(__name__)


@app.route('/success')
def success():
    return "Success"


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'first_name': 'Michael', 'last_name': "Choi"},
        {'first_name': 'John', 'last_name': "Supsupin"},
        {'first_name': 'Mark', 'last_name': "Guillen"},
    ]
    # index = 1
    return render_template("HTML_table.html", students=student_info)


# app.run(debug=True) should be the very last statement!
if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
