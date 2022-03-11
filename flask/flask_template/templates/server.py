# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following


@app.route('/')
def index():
    # Return the string 'Hello World!' as a response AUTOMATICALLY without expressing an invokation
    return render_template('index.html', phrase="hello", times=5)
    # return '<h1>Index Route. Hello, Flask!<h1>'
# # import statements, maybe some other routes
# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# 👇🏼


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
