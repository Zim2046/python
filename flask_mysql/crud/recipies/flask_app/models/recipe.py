from curses.ascii import isalpha
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
DATABASE = 'recipes_schema'

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.under_thirty = data['under_thirty']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.made_on = data['made_on']

    #TODO SAVE class method
    @classmethod
    def save(cls, data:dict ) -> int:
        print(data)
        query = "INSERT INTO recipes (name, under_thirty, description, made_on, instructions, user_id) VALUES ( %(name)s, %(under_thirty)s, %(description)s, NOW(), %(instructions)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )
    
    #TODO GET all class method
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    
    #TODO GET by name class method
    #👇 used in user validation
    @classmethod
    def get_by_name(cls,data:dict) -> object or bool:
        query = "SELECT * FROM recipes WHERE name = %(name)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        #👇 Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0]) #👈 This returns the first Dictionary that's stored in the List(which is the only one in it actually)

    #TODO GET by id class method
    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # comes back with a row  for a  ID 
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])
    
    #TODO UPDATE class method
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, under_thirty=%(under_thirty)s,description=%(description)s,instructions=%(instructions)s WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    #TODO VALIDATE class method
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our user
    @staticmethod                   #👇 indicates that it returns a boolean 
    def validate_recipe(recipe:dict) -> bool:
        is_valid = True # 👈 we assume this is true 
        data = { 'name' : recipe['name'] }
        if len(recipe['name']) < 2 :
            flash("Name must be at least 2 characters")
            is_valid = False
        if Recipe.get_by_name(data):
            flash(f"A recipe with the name {recipe['name']} already exists.")
            is_valid = False
        if len(recipe['description']) < 1:
            flash("A desscription is needed.")
            is_valid = False
        if len(recipe['instructions']) < 1:
            flash("Instructions are needed.")
            is_valid = False
        # 👇 test whether a field matches the pattern
        return is_valid
    
    #TODO DELETE class method
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    #TODO SHOW class method
    @classmethod
    def show(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # comes back as a new row ID
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])
    
