from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


DATABASE = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data):
        print("in method", data)
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        test = connectToMySQL(DATABASE).query_db(query, data)
        print("in method", test)
        return test
    
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our ninja
    @staticmethod
    def validate_ninja(ninja):
        is_valid = True # we assume this is true
        if len(ninja['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(ninja['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if int(ninja['age']) < 18:
            flash("Come back next year")
            is_valid = False
        return is_valid