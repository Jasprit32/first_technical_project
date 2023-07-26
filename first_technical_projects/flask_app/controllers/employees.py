from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models import employee
from flask_app.models import user
from flask_app.models import location

@app.route("/new/employee")
def new_employee():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id":session["user_id"]
    }
    return render_template("new_employee.html",user=user.User.get_by_id(data),location=location.Location.get_all())


@app.route("/create/employee",methods=["POST"])
def create_employee():
    if "user_id" not in session:
        return redirect("/logout")
    # if not Trip.validate_trip(request.form):
    #     return redirect("/new/trip")
    data = {
        "name" : request.form["name"],
        "email" : request.form ["email"],
        "phone": request.form [ "phone"],
        "address": request.form["address"],
        "user_id" : session["user_id"],
        "location_id":request.form["location_id"]

    }
    print(data)
    employee.Employee.save(data)
    return redirect("/dashboard")

# @app.route("/edit/employee/<int:id>")
# def edit_employee(id):
#     if "user_id" not in session:
#         return redirect("/logout")
#     data={
#         "id":id
#     }
#     user_data={
#         "id":session["user_id"]
#     }
#     return render_template("edit_employee.html",edit=employee.Employee.get_one(data),
#     user= user.User.get_by_id(user_data))

# @app.route("/update/employee",methods=["POST"])
# def update_employee():
#     if "user_id" not in session:
#         return redirect("/logout")
#     # if not Trip.validate_trip(request.form):
#     #     return redirect("/new/trip")
#     data = {
#         "name" : request.form["name"],
#         "email" : request.form ["email"],
#         "phone": request.form [ "phone"],
#         "address" : request.form["address"],
#         "user_id" : session["user_id"]
#     }
    
#     employee.Employee.update(data)
#     return redirect("/dashboard")

# @app.route("/employee/<int:id>")
# def show_employee(id):
#     if "user_id" not in session:
#         return redirect("/logout")
#     data={
#         "id":id
#     }
#     user_data={
#         "id":session["user_id"]
#     }
#     return render_template("show_employee.html",employee=employee.Employee.get_one(data),
#     user=user.User.get_by_id(user_data))

# @app.route("/destroy/employee/<int:id>")
# def destroy_employee(id):
#     if "user_id" not in session:
#         return redirect("/logout")
#     data={
#         "id":id
#     }
#     employee.Employee.destroy(data)
#     return redirect("/dashboard")

