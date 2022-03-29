from flask_app.config.mysqlconnection import connectToMySQL
from curses.ascii import isalpha
from flask_app import flash, re
                            #👆 the regex module
DATABASE = 'recipes_schema'
#👇 create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    #👇 used in user validation
    @classmethod
    def get_by_email(cls,data:dict) -> object or bool:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        #👇 Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0]) #👈 This returns the first Dictionary that's stored in the List(which is the only one in it actually)

    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our user
    @staticmethod                   #👇 indicates that it returns a boolean 
    def validate_user(user:dict) -> bool:
        is_valid = True # 👈 we assume this is true 
        data = { "email" : user["email"] }
        
        if len(user['first_name']) < 2 or not user['first_name'].isalpha():
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2 or not user['last_name'].isalpha():
            flash("Last name must be at least 2 characters.")
            is_valid = False
        # 👇 test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if User.get_by_email(data):
            flash("A user with this email already exists.")
            is_valid = False
        if user['password'] != user['confirm-password']:
            flash("Passwords do not match")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password needs to be at least 8 characters")
            is_valid = False
        return is_valid