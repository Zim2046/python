from flask import Flask, request  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes

# 2)


@app.route('/dojo')
def dojo():
    return "Dojo!"

# 3)


@app.route('/say/<string:name>')
def hello(name):
    return f'Hi {name}!'

# 4)
# for a route '/users/____/____', two parameters in the url get passed as username and id


@app.route('/repeat/<int:num>/<string:name>')
def show_user_profile(num, name):
    return f'{name*num}'

# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."


# @app.route('/<input>')
# def hello_world(input):
#     a = 'dojo'
#     b = 'say/<string:name>'
#     c = 'repeat/<int:num>/<string:name>'
#     if
#     return 'Sorry! No response. Try again.'

# @app.route('/<input>')
# def show_user_profile(input):
#     return 'Sorry! No response. Try again.'
# # app.run(debug=True) should be the very last statement!f


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
