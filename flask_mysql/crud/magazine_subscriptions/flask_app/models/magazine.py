from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'magazine_subscription_red'

class Magazine:
    def __init__( self , data ):
        self.id = data['id']
        self.description = data['description']
        self.title = data['title']
        self.user_id = data['user_id']
        # self.first_name = data['first_name'] #TODO used in the JOIN at 'get_user_with_magazines' and now must be added here to be correct
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#TODO CREATE
#TODO class method to add a magazine to the DB 
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO magazines (title, description, user_id) VALUES ( %(title)s, %(description)s, %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db( query, data )
        # print(result)
        return result
        #TODO the return stmt returns the id as an int of the magazine created

#TODO READ
    @classmethod
    def get_all_both(cls) -> list:
        query = "SELECT * FROM magazines JOIN users ON users.id = magazines.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        magazines_users = []
        for magazine in results: #TODO taking dicts from DB and making magazine objects
            magazines_users.append(magazine)
        # pprint(magazines)
        return magazines_users
    
    # @classmethod
    # def get_all(cls) -> list:
    #     query = "SELECT * FROM magazines;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     print(results)
    #     magazines = []
    #     for magazine in results: #TODO taking dicts from DB and making magazine objects
    #         magazines.append( cls(magazine) )
    #     # pprint(magazines)
    #     return magazines

#TODO READ
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM magazines WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])
    
#FIXME this needs to be update users!
#TODO UPDATE
    @classmethod
    def update(cls, data:dict) -> object:
        query = 'UPDATE magazines SET description=%(description)s, user_id=%(user_id)s WHERE id = %(id)s;'
        pprint(query)
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data:dict) -> object:
        query = 'DELETE FROM magazines WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#TODO  VALIDATION
    @staticmethod
    def validate_magazine(magazine:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(magazine['description']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(magazine['title']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        return is_valid