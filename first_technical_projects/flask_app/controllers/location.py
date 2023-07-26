from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.location import Location
from flask_app.controllers import users


@app.route("/new/location")
def new_location():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id":session["user_id"]
    }
    
    return render_template("dashboard.html",user=user.User.get_by_id(data),all_location=Location.get_all())

@app.route('/create/location',methods=['POST'])
def create_location():
    Location.save(request.form)
    return redirect('/dashboard')

# @app.route('/location/<int:id>')
# def show_location(id):
#     data = {
#         "id": id
#     }
#     return render_template('employee.html', dojo=Dojo.get_one_with_employee(data))