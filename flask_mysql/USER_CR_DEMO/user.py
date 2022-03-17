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
        # print("Nn get_all function", results)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for userRes in results:
            users.append(cls(userRes))
        return users

    @classmethod
    def save(cls, data):
        users = "INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # comes back as a new row ID
        results = connectToMySQL(DATABASE).query_db(users, data)
        # print(results)
        # WE DO NOT NEED TO ITERATE HERE!!!
        return results
