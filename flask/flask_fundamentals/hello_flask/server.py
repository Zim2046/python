from flask import Flask  # Import Flask to allow us to create our app
# Create a new instan  e of the Flask class called "app"
app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following


@app.route('/')
def hello_world():
    # Return the string 'Hello World!' as a response AUTOMATICALLY without expressing an invokation
    return 'Hello World!!'
# # import statements, maybe some other routes
# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# 👇🏼


@app.route('/hello/<username>/<int:id>')
def hello(username, id):
    print(username)
    print(id)
    return f'username: {username * id}'


@app.route('/success')
def success():
    return "success"

# app.run(debug=True) should be the very last statement!


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
