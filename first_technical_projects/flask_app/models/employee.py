from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Employee:
    db="non_stop_trucking"
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.email = data["email"]
        self.phone = data["phone"]
        self.address = data["address"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.location_id=data["location_id"]

    @classmethod
    def save(cls,data):
        query  = """INSERT INTO employee (name,email,phone,address,user_id,location_id)
                        VALUES(%(name)s,%(email)s,%(phone)s,%(address)s,%(user_id)s,%(location_id)s);"""
        return connectToMySQL(cls.db).query_db(query,data)
        print(query) 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM employee;"
        results = connectToMySQL(cls.db).query_db(query)
        all_employee = []
        for row in results:
            all_employee.append(cls(row))
        return all_employee

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM employee where id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

#     @classmethod
#     def update (cls,data):
#         query ="""UPDATE employee SET name=%(name)s,email=%(email)s,phone=%(phone)s,
#                     address=%(address)s,updated_at=NOW() WHERE id=%(id)s"""
#         return connectToMySQL(cls.db).query_db(query,data)

#     @classmethod
#     def destroy(cls,data):
#         query = "DELETE FROM employee WHERE id + %(id)s;"
#         return connectToMySQL(cls.db).query_db(query,data)


# # @staticmethod
# # def validate_trip(trip):
# #     is_valid = True
# #     if len(trip['name']) < 3:
# #         is_valid = False
# #         flash("name must be at least 3 characters","employee")
# #     if len