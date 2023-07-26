from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import employee

class Location:
    db="non_stop_trucking"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.location = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM location;"

        results = connectToMySQL(cls.db).query_db(query)
        location = []

        for d in results:
            location.append( cls(d) )
        return location

    @classmethod
    def save(cls, data):
        query= "INSERT INTO location (name) VALUES (%(name)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(1)
        print(result)
        print(2)
        return result


    @classmethod
    def get_one_with_employee(cls,data):
        query="""SELECT * FROM location LEFT JOIN employee ON employee.id = employee.location_id
                    WHERE location.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        location = cls(resutlt[0])
        for row in results:
            e = {
                "id":row["employee.id"],
                "name":row["name"],
                "email":row["email"],
                "phone": row["phone"],
                "address": row["address"],
                "created_at":row["created_at"],
                "updated_at":row["updated_at"]


            }
            employee_data = employee.Employee(employee_data)
            location.employee.append(employee_data)

        return location