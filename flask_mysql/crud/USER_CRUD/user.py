from pprint import pprint
from unittest import result
from flask import session
from mysqlconnection import connectToMySQL

DATABASE = "users_schema"


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):  # Gets 👇🏼 all of the instances of the class memebr made
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # results becomes a list(array) of dictionaries
        results = connectToMySQL(DATABASE).query_db(query)
        users = []  # Create an empty list to append our instances of users
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # comes back as a new row ID
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def view(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # comes back as a new row ID
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def getLastAdd(cls):
        query = "SELECT * FROM users ORDER BY ID DESC LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        return results[0]

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET  first_name=%(first_name)s, last_name=%(last_name)s,email=%(email)s,created_at=NOW(),updated_at=NOW() WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
