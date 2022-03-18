from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas_schema'


class Dojo:
    def __init__(self, data):
        self.dojo_id = data['dojo_id']
        self.name = data['name']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        print(dojos)
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojo = cls(results[0])
        # dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        print(dojos)
        return dojos
