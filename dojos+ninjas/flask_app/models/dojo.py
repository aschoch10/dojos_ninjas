from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


# Retreive all dojos method
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos


# Create new dojo method
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s);"
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        return results


# Show one dojo info
    @classmethod
    def showOne(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        if len(results) == 0:
            return False
        return Dojo(results[0])


# All ninjas from one dojo
    @classmethod
    def allNinjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        if len(results) == 0:
            return False
        dojo =  Dojo(results[0])

        if results[0]["ninjas.id"] != None:
            for row in results:
                ninja_data = {
                    **row, 
                    "id": row['ninjas.id'],
                    "dojo_id": row['dojo_id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age": row['age']
                }
                dojo.ninjas.append(ninja.Ninja(ninja_data ))

        return dojo
        
    









# # Update current user
#     @classmethod 
#     def update(cls, data):
#         query = 'UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id = %(id)s' 
#         results =  connectToMySQL('users_schema').query_db( query, data )
#         return results 

# # Destroy 
#     @classmethod
#     def destroy(cls, data):
#         query = 'DELETE FROM users WHERE id = %(id)s'
#         connectToMySQL('users_schema').query_db( query, data 
