
# Runthe below in your terminal to get started with you FLASK project
# pipenv install pymysql flask pipenv shell pip install cryptography
# then open your server python3 server.pyfrom flask_app import app
from flask_app import app
from flask_app.controllers import burgers
# ...server.py


if __name__ == "__main__":
    app.run(debug=True)
