from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from pprint import pprint
from flask_app.models.magazine import Magazine
from curses.ascii import isalpha

DATABASE = 'magazine_subscription_red'
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
        self.magazines = []
    
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL(DATABASE).query_db( query, data )
        return result

    #TODO used in user validation
    @classmethod
    def get_by_email(cls,data:dict) -> object or bool:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    #TODO get all of a user's magazines data and returns it as 'user'
    @classmethod 
    def get_user_with_magazines(cls, data):
        query = "SELECT * FROM users LEFT JOIN magazines ON magazines.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        print(results[0])
        user = cls(results[0])
        print(user)
        
        for result in results:
            magazine_data = { 
                'id': result['magazines.id'],
                'description': result['description'],
                'title': result['title'],
                'user_id': result['user_id'],
                'first_name': result['first_name'], #TODO refer to magazine Class when making Magazine
                'created_at': result['magazines.created_at'],
                'updated_at': result['magazines.updated_at'],
            }
            user.magazines.append(Magazine(magazine_data))
            print(user)
        return user

    @staticmethod
    def validate_user(user:dict) -> bool:
          is_valid = True # 👈 we assume this is true 
          data = { "email" : user["email"] }

          if len(user['first_name']) < 3 or not user['first_name'].isalpha():
              flash("First name must be at least 3 characters.")
              is_valid = False
          if len(user['last_name']) < 3 or not user['last_name'].isalpha():
              flash("Last name must be at least 3 characters.")
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