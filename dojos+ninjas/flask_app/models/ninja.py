from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__ (self, data):
        self.id = data['id']
        self.dojo_id = data ['dojo_id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # New ninja, when queried returns ID
    @classmethod
    def newNinja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )


    # # Returns all ninjas when queried 
    # def allNinjas(cls, data):
    #     query = "SELECT * FROM ninjas;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    #     # Create an empty list to append our instances of friends
    #     ninjas = []
    #     # Iterate over the db results and create instances of users with cls.
    #     for ninja in results:
    #         ninjas.append( cls(ninja) )
    #     return ninjas
